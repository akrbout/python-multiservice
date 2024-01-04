from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    engine: str
    user: str
    password: str
    host: str
    port: str
    name: str

    @property
    def connection_string(self) -> str:
        if self.engine == "postgresql":
            return f"{self.engine}+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        else:
            return f"{self.engine}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    class Config:
        env_prefix = "DATABASE_"


class AuthSettings(BaseSettings):
    secret: str
    reset_secret: str
    verification_secret: str
    algorithm: str

    class Config:
        env_prefix = "AUTH_"


class BaseIntegrationSettings(BaseSettings):
    host: str
    port: str

    @property
    def service_address(self) -> str:
        return f"http://{self.host}:{self.port}"


class AvatarGeneratorSettings(BaseIntegrationSettings):
    image_size: int

    class Config:
        env_prefix = "AVATAR_SERVICE_"


auth_settings = AuthSettings()
database_settings = DatabaseSettings()
avatar_generator_settings = AvatarGeneratorSettings()
