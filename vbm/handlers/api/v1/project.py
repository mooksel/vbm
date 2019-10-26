from aiohttp.web_urldispatcher import UrlDispatcher
from marshmallow import Schema, fields, post_load

import datetime

from vbm.models import Project

from . import BaseHandler


class CreateProjectSchema(Schema):
    name = fields.String()


class ProjectHandler(BaseHandler):

    def register(self, router: UrlDispatcher):
        router.add_post(f"{self.path}", self.create_project)

    async def create_project(self, request):
        pass
        # payload = await project.json()

        # schema = CreateProjectSchema()
        # project_data = schema.load(payload["data"])

        # project = self.daos.project_dao.create(name=project_data["name"])
        # # return
