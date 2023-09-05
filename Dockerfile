
FROM python:3.11-slim

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY .src /app/src

ENTRYPOINT [ "python", "src/main.py" ]