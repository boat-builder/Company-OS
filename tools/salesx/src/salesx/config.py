"""Configuration loading.

Credentials come from environment variables, falling back to a `.env` file beside
the package root (so the CLI works both in a shell with a .env and in CI where
secrets are injected as env vars). Validation is lazy: a command only requires the
credentials for the providers it actually touches, so you can use `crm` with only
a Close key, or `intel`/`enrich` with only the Marketing key.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .errors import ConfigError

# .env lives in the project root: src/salesx/config.py -> parents[2] == project dir.
_ENV_PATH = Path(__file__).resolve().parents[2] / ".env"


def _read_env_file() -> dict[str, str]:
    values: dict[str, str] = {}
    if _ENV_PATH.exists():
        for line in _ENV_PATH.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            values[key.strip()] = val.strip().strip('"').strip("'")
    return values


def _pick(name: str, file_env: dict[str, str], default: str = "") -> str:
    """Env var wins over .env file wins over default."""
    return os.environ.get(name) or file_env.get(name, default)


@dataclass(frozen=True)
class Settings:
    marketing_api_key: str
    marketing_base_url: str
    marketing_auth_style: str
    close_api_key: str

    def require_marketing(self) -> "Settings":
        if not self.marketing_api_key:
            raise ConfigError(
                "MARKETING_API_KEY is not set.\n"
                "Add it to tools/salesx/.env (copy .env.example) or export it:\n"
                "    MARKETING_API_KEY=mk_live_xxxxx"
            )
        if not self.marketing_base_url:
            raise ConfigError(
                "MARKETING_BASE_URL is not set.\n"
                "Add the backend host to .env (or export it):\n"
                "    MARKETING_BASE_URL=https://your-backend-host"
            )
        return self

    def require_close(self) -> "Settings":
        if not self.close_api_key:
            raise ConfigError(
                "CLOSE_API_KEY is not set.\n"
                "Add it to tools/salesx/.env (or export it):\n"
                "    CLOSE_API_KEY=api_xxxxx"
            )
        return self


@lru_cache(maxsize=1)
def load_settings() -> Settings:
    file_env = _read_env_file()
    return Settings(
        marketing_api_key=_pick("MARKETING_API_KEY", file_env),
        marketing_base_url=_pick("MARKETING_BASE_URL", file_env).rstrip("/"),
        marketing_auth_style=_pick("MARKETING_AUTH_STYLE", file_env, "bearer").lower(),
        close_api_key=_pick("CLOSE_API_KEY", file_env),
    )
