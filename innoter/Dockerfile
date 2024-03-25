FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

