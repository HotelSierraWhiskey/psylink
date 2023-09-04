from config import config, get_config, logger
from db import get_db
import json


def handle_command(message):
    db = get_db()

    logger.info(f'Received command {message}')

    command = message['input']['command']
    args = message['input']['args']

    payload = message

    if command == 'ping':
        payload["output"] = "pong"

    if command == 'set_config':
        global config
        config = get_config(args)
        payload["output"] = "ok"

    db.lpush(config.redis.command_output_queue, json.dumps(payload))
