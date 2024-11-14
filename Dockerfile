# Dockerfile
FROM python:3.11

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8080

# Flaskを5001ポートで実行する
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]