FROM python:3.10-buster

WORKDIR /app

COPY ./src/ ./src/

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE ${PORT}

WORKDIR /app/src

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]