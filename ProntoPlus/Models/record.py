import marshmallow as mw
import datetime as dt
import uuid
import dataclasses as da
import sqlalchemy as sa
import sqlalchemy_utils as sau
import sqlalchemy.orm as orm

import ProntoPlus.Models._db as _db
import ProntoPlus.Models.base_model as _base


@da.dataclass
class Record(_base.Base):
    id_user: uuid.UUID = da.field(default_factory=lambda: None)
    id_patient: uuid.UUID = da.field(default_factory=lambda: None)
    text: str = da.field(default_factory=lambda: None)
    created_date: dt.datetime = da.field(default_factory=lambda: dt.datetime.now())
    last_modified_date: dt.datetime = da.field(default_factory=lambda: None)

    def __post_init__(self):
        if self.last_modified_date is None:
            self.last_modified_date = self.created_date


class RecordSchema(mw.Schema):
    @mw.validates('last_modified_date')
    def must_be_higher_than_creation(self, data, **kwargs):
        if data and data < self.created_date:
            raise mw.ValidationError(f'Last modified date is before creation date')

    id_user = mw.fields.UUID(required=True, allow_none=False)
    id_patient = mw.fields.UUID(required=True, allow_none=False)
    text = mw.fields.Str(required=True, allow_none=False)
    created_date = mw.fields.DateTime(required=True)
    last_modified_date = mw.fields.DateTime()

    @mw.post_load
    def _make(self, data, **kwargs):
        return Record(**data)


recordTable = sa.Table(
    'records',
    _db.Model.metadata,
    sa.Column('id', sau.UUIDType, primary_key=True, unique=True, nullable=False),
    sa.Column('id_user', sau.UUIDType, sa.ForeignKey('users.id'), nullable=False),
    sa.Column('id_patient', sau.UUIDType, sa.ForeignKey('patients.id'), nullable=False),
    sa.Column('id_tenant', sau.UUIDType, sa.ForeignKey('tenants.id'), nullable=False),
    sa.Column('created_date', sa.DateTime, nullable=False),
    sa.Column('last_modified_date', sa.DateTime),
    sa.Column('text', sa.Text)
)

orm.mapper(Record, recordTable)
