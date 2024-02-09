"""Collects all routes for the application.

If you plan to create a custom application with only some of the routes
then create your own ``api.py`` file and import the routes you need from
the ``{{ cookiecutter.project_slug }}.server`` module, then create a ``main.py`` file that
uses this api modeled on the ``main.py`` file in this directory.
"""
from typing import cast

from .app import FastAPI, app
from .xxx.api import router as xxx_router


app = cast(FastAPI, app)
app.include_router(xxx_router)

