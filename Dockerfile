FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt /app/

COPY . /app/

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]