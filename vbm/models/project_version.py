import enum
import datetime

from .base import Base


class ProjectVersionStrategy(enum.Enum):
    CALVER = "CALVER"
    SEMVER = "SEMVER"


class ProjectVersion(Base):

    def __init__(
        self,
        identifier: int,
        version_strategy: ProjectVersionStrategy,
        project_identifier: int,
        creation_datetime: datetime.datetime,
    ):
        super().__init__(
            identifier=identifier,
            creation_datetime=creation_datetime
        )

        self._version_strategy = version_strategy
        self._project_identifier = project_identifier

    @property
    def version_strategy(self) -> ProjectVersionStrategy:
        return self._version_strategy

    @property
    def project_identifier(self) -> int:
        return self._project_identifier
