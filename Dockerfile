FROM python:latest

WORKDIR /home/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3", "server.py"]