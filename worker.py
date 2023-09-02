from config import get_config
from db import get_db
from llm import get_llm


config = get_config()
db = get_db()
llm = get_llm()


def worker_task():
    _, prompt = db.brpop(config.redis.input_queue)
    output = llm(str(prompt))
    db.lpush(config.redis.output_queue, str(output))
