from aiohttp.web_urldispatcher import UrlDispatcher

from vbm.daos import DAOSContainer

from .base_handler import BaseHandler
from .api import APIHandler


class RootHandler(BaseHandler):

    def __init__(
        self,
        path: str,
        daos: DAOSContainer,
    ):
        super().__init__(
            path=path,
            daos=daos,
        )

        self._api = APIHandler(
            path=f"{path}/api",
            daos=daos,
        )

    def register(self, router: UrlDispatcher):
        self._api.register(router=router)

