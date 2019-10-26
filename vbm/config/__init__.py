import typing as t

from .server import ServerConfig


class Config(t.NamedTuple):
    server: ServerConfig

    @classmethod
    def from_environ(cls, environ: t.Mapping):
        return cls(
            server=ServerConfig.from_environ(environ=environ),
        )
