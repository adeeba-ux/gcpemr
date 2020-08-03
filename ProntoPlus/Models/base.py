import dataclasses as da
import uuid
import marshmallow as mw
import abc
import typing as t


@da.dataclass()
class Base(abc.ABC):
    tenant: uuid.UUID
    id: uuid.UUID = da.field(default_factory=lambda: uuid.uuid4())
    presentation: t.Dict = None


class BaseSchema(mw.Schema):
    id = mw.fields.UUID()
    tenant = mw.fields.UUID(required=True)
