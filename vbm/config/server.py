import typing as t


class ServerConfig(t.NamedTuple):

    port: int

    @classmethod
    def from_environ(cls, environ: t.Mapping):
        return cls(
            port=environ["CONFIG_SERVER_PORT"],
        )
