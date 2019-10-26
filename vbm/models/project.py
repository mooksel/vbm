import datetime

from .base import Base


class Project(Base):

    def __init__(
        self,
        identifier: int,
        name: str,
        creation_datetime: datetime.datetime
    ):
        super().__init__(
            identifier=identifier,
            creation_datetime=creation_datetime
        )

        self._name = name

    @property
    def name(self) -> str:
        return self._name
