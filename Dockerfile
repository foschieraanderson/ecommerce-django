FROM python:3.8

# python:
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
# pip:
  PIP_DISABLE_PIP_VERSION_CHECK=on \
# poetry:
  POETRY_VERSION=1.1.5 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install poetry==$POETRY_VERSION

WORKDIR /www

ADD pyproject.toml poetry.lock www/

ADD . .

RUN poetry install