# Dockerfile
FROM python:3.11

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Flaskを5001ポートで実行する
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]