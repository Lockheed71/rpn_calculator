from python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
COPY server.py server.py
COPY app/ app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000