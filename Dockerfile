FROM python:3.11.0-slim

ENV POETRY_VIRTUALENVS_CREATE=false

ENV FLASK_APP=src.infra.api.api

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN poetry install

CMD ["flask", "run", "--host=0.0.0.0"]
