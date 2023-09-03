from config import get_config, logger
from db import get_db
from llm import get_llm
import json


config = get_config()
db = get_db()
llm = get_llm()


def worker_task():
    _, input_data = db.brpop(config.redis.input_queue)
    json_data = json.loads(input_data.decode('utf-8').replace("'", '"'))

    id = json_data['id']
    priority = json_data['priority']
    prompt = json_data['input']

    if not config.properties.max_priority >= priority >= config.properties.min_priority:
        db.lpush(config.redis.input_queue, json.dumps(json_data))
        return

    logger.info(f"Pulled message {id} from input queue")

    output = llm(prompt, **config.llama_params)

    logger.info(f"Done. {output}")

    payload = json.dumps({'id': id, 'hostname': config.connection.hostname,
                          'input': prompt, 'output': output})

    db.lpush(config.redis.output_queue, payload)
