FROM python:3.13-slim

RUN groupadd -r survey && useradd -r -g survey survey

WORKDIR /app

# 기반 이미지가 Debian 보안 수정을 늦게 싣는다. 빌드 때 apt 보안 판까지 올린다
# (2026-11-19 zlib +deb13u1 — Docker Hub python:3.13-slim에는 아직 없다).
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R survey:survey /app
USER survey

ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Seoul

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=10s \
    CMD curl -f http://localhost:8000/api/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
