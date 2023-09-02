import dotmap
import tomllib


def get_config():
    try:
        with open('config.toml', mode='rb') as file:
            config = tomllib.load(file)
            return dotmap.DotMap(config)
    except tomllib.TOMLDecodeError as e:
        print(f'Malformed config file\n{e}')
    except FileNotFoundError:
        print("Couldn't locate config.toml")
