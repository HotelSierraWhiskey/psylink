from config import get_config
import redis


def get_db():
    config = get_config()
    db = redis.StrictRedis(host=config.redis.host,
                           port=config.redis.port,
                           db=config.redis.db,
                           password=config.redis.password)
    return db
