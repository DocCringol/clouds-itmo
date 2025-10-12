FROM python:3.11-slim AS dependencies

RUN --mount=type=cache,target=/var/lib/apt/lists apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip && \
    pip install -r requirements.txt

FROM python:3.11-slim AS runtime

WORKDIR /app

COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dependencies /usr/local/bin /usr/local/bin

COPY main.py .

EXPOSE 8080

CMD ["python", "main.py"]