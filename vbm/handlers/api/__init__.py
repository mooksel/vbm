from aiohttp.web_urldispatcher import UrlDispatcher

from vbm.handlers.base_handler import BaseHandler
from vbm.daos import DAOSContainer

from .v1 import V1Handler


class APIHandler(BaseHandler):

    def __init__(
        self,
        path: str,
        daos: DAOSContainer,
    ):
        super().__init__(
            path=path,
            daos=daos,
        )

        self._v1 = V1Handler(
            path=f"{path}/v1",
            daos=daos,
        )

    def register(self, router: UrlDispatcher):
        self._v1.register(router=router)
