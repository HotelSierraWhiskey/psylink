from config import config
import redis


def get_db():
    db = redis.StrictRedis(host=config.redis.host,
                           port=config.redis.port,
                           db=config.redis.db,
                           password=config.redis.password)
    return db
