FROM python:3.10-slim
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask requests

EXPOSE 8000

CMD ["python", "app.py"]
