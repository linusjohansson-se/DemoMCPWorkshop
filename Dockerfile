FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["fastmcp", "run", "/app/main.py", "--transport", "http", "--host", "0.0.0.0", "--port", "8000"]
