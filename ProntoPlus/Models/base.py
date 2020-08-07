import dataclasses as da
import uuid
import marshmallow as mw
import abc
import typing as t
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')


@da.dataclass()
class Base(abc.ABC):
    tenant: uuid.UUID
    id: uuid.UUID = da.field(default_factory=lambda: uuid.uuid4())
    presentation: t.Dict = None


class BaseSchema(mw.Schema):
    class Meta:
        datetimeformat = cfg['CLIENT']['dateformat']

    id = mw.fields.UUID()
    tenant = mw.fields.UUID(required=True)
