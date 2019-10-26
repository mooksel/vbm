from abc import ABC, abstractmethod

from aiohttp.web_urldispatcher import UrlDispatcher

from vbm.daos import DAOSContainer


class BaseHandler(ABC):

    def __init__(
        self,
        path: str,
        daos: DAOSContainer,
    ):
        self._path = path
        self._daos = daos

    @property
    def path(self) -> str:
        return self._path

    @property
    def daos(self) -> DAOSContainer:
        return self._daos

    @abstractmethod
    def register(self, router: UrlDispatcher):
        raise NotImplementedError()
