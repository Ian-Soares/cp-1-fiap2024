FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app/* /app

RUN rm requirements.txt

EXPOSE 8090

CMD ["uvicorn", "main:app", "--port", "8090", "--host", "0.0.0.0"]