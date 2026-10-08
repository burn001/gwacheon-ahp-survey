import os
from functools import lru_cache


def _mongodb_uri() -> str:
    # MONGODB_URI_FILE이 있으면 그 파일 내용(앞뒤 공백·개행 제거)을 URI로 쓴다 — 운영은 compose secrets로
    # 파일을 마운트해 docker inspect·compose config에 비밀번호가 평문으로 보이지 않게 한다(2026-10-08).
    uri_file = os.getenv("MONGODB_URI_FILE")
    if uri_file:
        with open(uri_file, encoding="utf-8") as f:
            uri = f.read().strip()
        if not uri:
            raise RuntimeError(f"MONGODB_URI_FILE is empty: {uri_file}")
        return uri
    return os.getenv("MONGODB_URI", "mongodb://localhost:27017")


class Settings:
    MONGODB_URI: str = _mongodb_uri()
    MONGODB_DB: str = os.getenv("MONGODB_DB", "gwacheon_ahp_survey")
    TOKEN_SECRET: str = os.getenv("TOKEN_SECRET", "change-me-in-production")
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")
    API_PREFIX: str = "/api"
    ADMIN_KEY: str = os.getenv("ADMIN_KEY", "change-me-admin-key")
    GMAIL_USER: str = os.getenv("GMAIL_USER", "")
    GMAIL_APP_PASSWORD: str = os.getenv("GMAIL_APP_PASSWORD", "")
    SURVEY_BASE_URL: str = os.getenv("SURVEY_BASE_URL", "https://example.com/survey")

@lru_cache
def get_settings() -> Settings:
    return Settings()
