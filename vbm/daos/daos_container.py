from .abcs import ProjectDAO


class DAOSContainer:

    def __init__(
        self,
        project_dao: ProjectDAO,
    ):
        self._project_dao = project_dao

    @property
    def project_dao(self) -> ProjectDAO:
        return self._project_dao
