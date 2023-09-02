from worker import worker_task


if __name__ == '__main__':
    print('Running...')
    while True:
        try:
            worker_task()
        except KeyboardInterrupt:
            quit()
