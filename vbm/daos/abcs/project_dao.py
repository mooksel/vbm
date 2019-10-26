from abc import ABC, abstractmethod

from vbm.models import Project


class ProjectDAO(ABC):

    @abstractmethod
    def create(self, name: str) -> Project:
        raise NotImplementedError()


    @abstractmethod
    def get_by_name(self, project_name: str) -> Project:
        raise NotImplementedError()
