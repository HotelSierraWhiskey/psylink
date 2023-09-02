from config import get_config
from llama_cpp import Llama


def get_llm():
    config = get_config()
    llm = Llama(model_path=config.llama.model_path, verbose=False)
    return llm
