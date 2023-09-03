from worker import worker_task
from config import get_config, logger


config = get_config()

if __name__ == '__main__':
    logger.info("Starting Psylink worker...")
    logger.info(f"Running on {config.connection.hostname} ({config.connection.ip})")
    while True:
        try:
            worker_task()
        except KeyboardInterrupt:
            quit()
