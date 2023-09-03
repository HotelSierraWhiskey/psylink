from config import get_config
from db import get_db
from llm import get_llm
import json
import socket
from log import logger


config = get_config()
db = get_db()
llm = get_llm()


def worker_task():
    _, input_data = db.brpop(config.redis.input_queue)
    json_data = json.loads(input_data.decode('utf-8').replace("'", '"'))
    logger.info("Received data from input queue")
    priority = json_data['priority']
    prompt = json_data['input']

    
    if not config.properties.max_priority >= priority >= config.properties.min_priority:
        db.lpush(config.redis.input_queue)
        logger.info(f"Priority mismatch")
        return

    hostname = socket.gethostname()
    
    output = llm(prompt, **config.llama_params)
    logger.info(f"processed prompt: {output}")
    payload = str({'hostname': hostname, 'input': prompt, 'output': output})
    db.lpush(config.redis.output_queue, payload)