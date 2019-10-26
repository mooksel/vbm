import enum
import datetime

from .base import Base


class ProjectBuild(Base):

    def __init__(
        self,
        identifier: int,
        version_identifier: int,
        build_numder: int,
        creation_datetime: datetime.datetime,
    ):
        super().__init__(
            identifier=identifier,
            creation_datetime=creation_datetime
        )

        self._version_identifier = version_identifier
        self._build_numder = build_numder

    @property
    def version_identifier(self) -> int:
        return self._version_identifier

    @property
    def build_number(self) -> int:
        return self._build_numder
