FROM python:3.12.0-slim-bullseye AS compile-image

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-dev libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
RUN python3 -m venv ${VIRTUAL_ENV}

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
