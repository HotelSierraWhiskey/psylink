# Psylink

A backend and minimal protocol for distributing local LLM prompts.
Built using Llama CPP for Python, and Redis.

```
Client -------\                           /--------- Psylink Worker
               \                         /
Client ---------- Redis Message Queues ------------- Psylink Worker
               /                         \
Client -------/                           \--------- Psylink Worker
```

### Requirements

- Python >= 3.11
- A Redis server
- A Llama CPP-compatible LLM model

Create a virtual environment and run 

`pip install -r requirements.txt`

to install the required python packages.

### Psylink Message Format

Client input queue message format:

```python
{
    "message_id": str,
    "priority": int,
    "input": str
}
```

Client command queue message format:

```python
{
    "message_id": str,
    "worker_id": str,
    "input": {
        "command": str,
        "args": dict | None
    }
}
```

Worker output queue message format:

```python
{
    "message_id": str,
    "worker_id": str,
    "input": str,
    "output": str
}
```

Example config.toml:

```toml
[redis]
host = "localhost"
port = 6379
password = "supersecretpassword"
db = 0
prompt_input_queue = "psy_prompt_input_queue"
prompt_output_queue = "psy_prompt_output_queue"
command_input_queue = "psy_command_input_queue"
command_output_queue = "psy_command_output_queue"

[model]
model_path = "models/codellama-13b-instruct.Q8_0.gguf"

[llama_params]
max_tokens = 32
echo = true
temperature = 0.85

[properties]
min_priority = 1
max_priority = 5
```