from marshmallow import Schema, fields, post_load, ValidationError, validates_schema
from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Record:
    id_user: UUID
    id_patient: UUID
    id_tenant: UUID
    text: str
    id: UUID = None
    created_date: datetime = datetime.now()
    last_modified_date: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid4()

        if self.last_modified_date is None:
            self.last_modified_date = self.created_date


class RecordSchema(Schema):
    @validates_schema
    def must_be_higher_than_creation(self, data, **kwargs):
        created_date = data.get('created_date', None)
        if created_date is None:
            created_date = datetime.now()
        last_modified_date = data.get('last_modified_date', None)

        if last_modified_date and last_modified_date < created_date:
            raise ValidationError(f'Last modified date is before creation date')

    id_user = fields.UUID()
    id_patient = fields.UUID()
    id_tenant = fields.UUID()
    id = fields.UUID()
    created_date = fields.DateTime()
    last_modified_date = fields.DateTime()
    text = fields.Str()

    @post_load
    def _make(self, data, **kwargs):
        return Record(**data)
