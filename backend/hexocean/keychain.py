from pydantic_settings import BaseSettings


class Keychain(BaseSettings):
    """
    Environment variables
    """
    secret_key: str

    postgres_username: str
    postgres_password: str

    postgres_host: str
    postgres_db: str
    postgres_port: str

    pgadmin_email: str
    pgadmin_password: str

    allowed_hosts: str


keychain = Keychain(_env_file="./.env", _env_file_encoding="utf-8")
