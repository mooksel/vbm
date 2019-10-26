import typing as t
import datetime

from abc import ABC


class Base(ABC):

    def __init__(
        self,
        identifier: int,
        creation_datetime: datetime.datetime,
    ):
        self._identifeir = identifier
        self._creation_datetime = creation_datetime

    @property
    def identifier(self) -> int:
        return self._identifeir

    @property
    def creation_datetime(self):
        return self._creation_datetime

    def to_dict(self):
        return {
            "identifier": self.identifier,
            "creation_datetime": self,
        }
