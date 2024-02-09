"""Server settings."""
import os
from typing import Any, Callable, List, Optional, Type, cast

from db4me import AllDatabaseSettings
from log2me import LogSettings
from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings
from pydantic_settings_yaml.base_settings import YamlConfigSettingsSource


class YamlBaseSettings(BaseSettings):
    """Allows to specify a 'yaml_file' path in the Config section.

    The secrets injection is done differently than in BaseSettings,
    allowing also partial secret replacement (such as
    "postgres://user:<file:path-to-password>@...").

    Default paths:

    - secrets_dir: "/etc/secrets" or env.SETTINGS_SECRETS_DIR
    - yaml_file: "/etc/config/config.yaml" or env.SETTINGS_YAML_FILE

    See also:

      https://pydantic-docs.helpmanual.io/usage/settings/

    Note:
      The content of this class was copied from pydantic_settings_yaml
      and modified to change the order of the sources of the settings.
    """

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        """
        Define the sources and their order for loading the settings values.

        Args:
            settings_cls: The Settings class.
            init_settings: The `InitSettingsSource` instance.
            env_settings: The `EnvSettingsSource` instance.
            dotenv_settings: The `DotEnvSettingsSource` instance.
            file_secret_settings: The `SecretsSettingsSource` instance.

        Returns:
            A tuple containing the sources and their order for
            loading the settings values.
        """
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )

    model_config = SettingsConfigDict(
        secrets_dir=os.environ.get(
            "SETTINGS_SECRETS_DIR",
            "/etc/secrets"
        ),
        yaml_file=os.environ.get(
            "SETTINGS_YAML_FILE", "/etc/config/config.yaml"
        ),
    )


class YamlSettingsConfigDict(SettingsConfigDict):
    yaml_file: str


class NetworkSettings(BaseModel):
    cors_origins: List[str] = Field(
        ["*"],
        description="The origins allowed to make CORS requests.",
    )
    cors_allow_credentials: bool = Field(
        True,
        description="Whether to allow credentials in CORS requests.",
    )
    cors_allow_methods: List[str] = Field(
        ["*"],
        description="The methods allowed in CORS requests.",
    )
    cors_allow_headers: List[str] = Field(
        ["*"],
        description="The headers allowed in CORS requests.",
    )


class Settings(YamlBaseSettings):
    """Server settings read from config file and from environment."""

    model_config = YamlSettingsConfigDict(
        env_prefix="{{ cookiecutter.env_prefix }}_",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        secrets_dir=os.environ.get(
            "{{ cookiecutter.env_prefix }}_SECRETS_LOCATION", "/run/secrets"
        ),
        yaml_file=os.environ.get("{{ cookiecutter.env_prefix }}_CONFIG", "config.yaml"),
    )

    log: LogSettings = Field(
        default_factory=cast(Callable[[], Any], LogSettings),
        description="Logging settings.",
    )

    database: AllDatabaseSettings = Field(
        default_factory=cast(Callable[[], Any], AllDatabaseSettings),
        description="Database settings.",
    )

    net: NetworkSettings = Field(
        default_factory=cast(Callable[[], Any], NetworkSettings),
        description="CORS settings.",
    )
