# Psylink

A backend and minimal protocol for distributing local LLM prompts.
Built using Llama CPP for python, and redis.

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
    "command": str
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
input_queue = "psy_input_queue"
output_queue = "psy_output_queue"

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