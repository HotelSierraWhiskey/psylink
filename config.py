import dotmap
import tomllib
import socket
import logging
import colorlog


def get_config():
    try:
        with open('config.toml', mode='rb') as file:
            config = tomllib.load(file)
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            config['connection'] = {'hostname': hostname, 'ip': ip}
            return dotmap.DotMap(config)
    except tomllib.TOMLDecodeError as e:
        print(f'Malformed config file\n{e}')
    except FileNotFoundError:
        print("Couldn't locate config.toml")


logger = logging.getLogger("psylink")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = colorlog.ColoredFormatter(
    "%(asctime)s [%(log_color)s%(levelname)s%(reset)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
    },
)

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
