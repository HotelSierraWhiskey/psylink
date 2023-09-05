from worker import worker_task
from config import config, logger


if __name__ == '__main__':
    logger.info(
        f"Starting Psylink (Worker UID: {config.properties.worker_id})")
    logger.info(
        f"Running on {config.connection.hostname} ({config.connection.ip})")

    try:
        worker_task()
    except KeyboardInterrupt:
        quit()
