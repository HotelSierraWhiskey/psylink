from config import config, logger
from db import get_db
from llm import get_llm
import json
import time
from commands import handle_command
from threading import Thread


db = get_db()
llm = get_llm()

expiration_time = 10


def prompt_event_listener():
    while True:
        _, input_data = db.brpop(config.redis.prompt_input_queue)
        json_data = json.loads(input_data.decode('utf-8').replace("'", '"'))

        current_time = time.time()

        if current_time - json_data['timestamp'] > expiration_time:
            return

        message_id = json_data['message_id']
        client_id = json_data['client_id']
        priority = json_data['priority']
        prompt = json_data['input']

        if not config.properties.max_priority >= priority >= config.properties.min_priority:
            db.lpush(config.redis.prompt_input_queue, json.dumps(json_data))
            return

        logger.info(f"Pulled message {message_id} from prompt input queue")

        output = llm(prompt, **config.llama_params)

        logger.info(f"Done. {output}")

        payload = json.dumps({'message_id': message_id,
                              'client_id': client_id,
                              'worker_id': config.properties.worker_id,
                              'input': prompt,
                              'output': output,
                              "timestamp": current_time})

        db.lpush(config.redis.prompt_output_queue, payload)


def command_event_listener():
    while True:
        input_data = db.lrange(config.redis.command_input_queue, 0, -1)
        current_time = time.time()

        for entry in input_data:
            command = json.loads(entry.decode('utf-8').replace("'", '"'))
            if current_time - command['timestamp'] > expiration_time:
                db.lrem(config.redis.command_input_queue, 0, entry)
            elif command["worker_id"] == config.properties.worker_id:
                handle_command(command)
                db.lrem(config.redis.command_input_queue, 0, entry)


def worker_task():
    t1 = Thread(target=prompt_event_listener)
    t2 = Thread(target=command_event_listener)
    t1.start()
    t2.start()
