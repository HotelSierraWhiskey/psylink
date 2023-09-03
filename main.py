from worker import worker_task
from log import logger


if __name__ == '__main__':
    logger.info("Starting Psylink...")
    while True:
        try:
            worker_task()
        except KeyboardInterrupt:
            quit()
