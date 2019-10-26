from aiohttp.web_urldispatcher import UrlDispatcher

from vbm.handlers.base_handler import BaseHandler
from vbm.daos import DAOSContainer

from .project import ProjectHandler


class V1Handler(BaseHandler):

    def __init__(
        self,
        path: str,
        daos: DAOSContainer,
    ):
        super().__init__(
            path=path,
            daos=daos,
        )

        self._project = ProjectHandler(
            path=f"{path}/projects",
            daos=daos,
        )

    def register(self, router: UrlDispatcher):
        self._project.register(router)
