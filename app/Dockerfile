FROM python:3.11-slim-bullseye as build-stage

RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends build-essential libpq-dev curl

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
ENV PATH=/opt/poetry/bin:$PATH

WORKDIR /app
COPY . /app

RUN poetry config virtualenvs.in-project true && poetry install --without dev

FROM python:3.11-slim as run-stage

COPY --from=build-stage /app /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
EXPOSE 8001

RUN sed -i 's/\r$//g' /app/bin/run
RUN chmod +x /app/bin/run
ENTRYPOINT [ "/app/bin/run" ]
