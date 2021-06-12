FROM python:3.9.5-slim as base

COPY requirements.txt /
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


FROM python:3.9.5-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONIOENCODING utf-8

COPY --from=base /wheels /wheels
COPY --from=base requirements.txt .

RUN pip install --no-cache /wheels/* && rm -rf /wheels && rm -rf /tmp* && rm requirements.txt
WORKDIR /app
COPY . /app
