"""The Flask application.

This is the module that should be imported when you want to add something
to the application.
"""
import pkgutil
from typing import Any, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from {{ cookiecutter.project_slug }}.schemas.errors import ErrorResponse


# The application singleton.
app: Optional[FastAPI] = None


def create_app(lifespan: Any, set_global: bool = False) -> FastAPI:
    """Create the FastAPI application.

    Args:
        lifespan: The lifespan manager for the FastAPI application.
        set_global: If True, set the global ``app`` variable to the
            created application. Defaults to False.
    Returns:
        The created FastAPI application.
    """
    global app

    # Read the description from the Markdown file.
    description = pkgutil.get_data(__name__, "app.md")
    assert description is not None

    # Create a new Flask application.
    result = FastAPI(
        title="{{ cookiecutter.project_name }} API",
        version="0.0.1",
        description=description.decode("utf-8"),
        responses={
            500: {
                "model": ErrorResponse,
                "description": "Internal server error.",
            }
        },
        lifespan=lifespan,
    )

    if set_global:
        app = result
    return result
