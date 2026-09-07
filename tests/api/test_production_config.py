"""La configuración de producción debe fallar cerrada."""

import pytest

from api.config import Settings


def production_settings(**overrides):
    values = {
        "environment": "production",
        "database_url": "postgresql://db.example/levelup",
        "jwt_secret_key": "x" * 40,
        "cors_origins": ["https://app.example"],
        "rate_limit_storage_uri": "redis://cache.example:6379/0",
    }
    values.update(overrides)
    return Settings(_env_file=None, **values)


def test_valid_production_configuration_passes():
    production_settings().validate_runtime()


@pytest.mark.parametrize(
    "override",
    [
        {"database_url": ""},
        {"jwt_secret_key": "short"},
        {"jwt_secret_key": "CHANGE_ME_IN_PRODUCTION_USE_A_LONG_RANDOM_STRING"},
        {"cors_origins": ["http://localhost:5173", "https://app.example"]},
        {"rate_limit_storage_uri": "memory://"},
    ],
)
def test_insecure_production_configuration_is_rejected(override):
    with pytest.raises(RuntimeError):
        production_settings(**override).validate_runtime()


def test_production_database_does_not_seed_demo_or_test_accounts(tmp_path, monkeypatch):
    from src.infrastructure.persistence.sqlite_repository import SQLiteRepository

    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.delenv("ADMIN_PASSWORD", raising=False)
    repo = SQLiteRepository(str(tmp_path / "production.db"))
    conn = repo.get_connection()
    try:
        usernames = {
            row[0]
            for row in conn.execute(
                "SELECT username FROM users WHERE username IN "
                "('profesor1', 'estudiante1', 'estudiante_colegio_1')"
            ).fetchall()
        }
    finally:
        conn.close()
    assert usernames == set()
