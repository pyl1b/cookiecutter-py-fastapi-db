import os

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr

schema = os.environ.get("{{ cookiecutter.env_prefix }}_DB_SCHEMA", "")


class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all models.

    Allows you to define a prefix for all the tables in the database
    and a schema for the database.
    """

    @declared_attr.directive
    def __tablename__(cls):
        tables_prefix = os.environ.get("{{ cookiecutter.env_prefix }}_TABLE_PREFIX", None)
        return (
            (tables_prefix + cls.__table_suffix__)
            if tables_prefix else cls.__table_suffix__
        )

    __table_args__ = {"schema": schema} if len(schema) else {}
