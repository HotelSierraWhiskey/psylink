# Psylink

A backend and minimal protocol for distributing local LLM prompts.
Built using Llama CPP for python, and redis.

### Psylink Message Format

Client message format:

```python
{
    "id": str,
    "priority": int,
    "input": str
}
```

Worker response format:

```python
{
    "id": str,
    "hostname": str,
    "input": str,
    "output": str
}
```