import typing as t
import os
import logging

from aiohttp import web

from vbm.models import Project, ProjectVersion, ProjectBuild
from vbm.handlers import RootHandler
from vbm.config import Config


log = logging.getLogger(__name__)


def init_logging():
    pass


def load_config() -> Config:
    return Config.from_environ(os.environ)


def create_app(config: Config) -> web.Application:
    app = web.Application()

    root_handler = RootHandler(
        path="/",
        daos=None,
    )

    root_handler.register(router=app.router)
    return app


if __name__ == "__main__":
    init_logging()
    log.info("Loading config ...")

    config = load_config()

    log.info("Config loaded")
    log.debug(config)

    app = create_app(config=config)
    web.run_app(app, port=config.server.port)
