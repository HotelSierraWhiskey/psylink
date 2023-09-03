# Psylink

### Psylink Message Format

Client message format:

```python
{
    "priority": int,
    "input": str
}
```

Worker response format:

```python
{
    "hostname": str,
    "input": str,
    "output": str
}
```