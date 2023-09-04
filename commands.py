from config import config, get_config, logger
from db import get_db
import json


def handle_command(message):
    db = get_db()

    logger.info(f'Received command {message}')

    message_id = message['message_id']
    worker_id = message['worker_id']
    input = message['input']
    command = message['input']['command']
    args = message['input']['args']

    data = {
        "message_id": message_id,
        "worker_id": worker_id,
        "input": input,
    }

    if command == 'ping':
        data["output"] = "pong"

    if command == 'set_config':
        global config
        config = get_config(args)
        data["output"] = "ok"

    db.lpush(config.redis.command_output_queue, json.dumps(data))
