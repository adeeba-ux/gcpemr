from marshmallow import Schema, fields, post_load, ValidationError, validates, validates_schema
from uuid import UUID
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class License:

    id: UUID
    tenant: UUID
    quota: int
    created_date: datetime
    expiration_date: datetime = None
    last_checked_date: datetime = None

    def __post_init__(self):
        if self.last_checked_date is None:
            self.last_checked_date = self.created_date


class LicenseSchema(Schema):
    @validates("quota")
    def must_be_at_least_one(self, data):
        if isinstance(data, int) and data < 1:
            raise ValidationError('Quota must be 1 or more.')

    @validates_schema
    def must_be_higher_than_creation(self, data, **kwargs):
        created_date = data.get('created_date', None)
        if created_date is None:
            created_date = datetime.now()
        
        expiration_date = data.get('expiration_date', None)
        last_checked_date = data.get('last_checked_date', None)

        if expiration_date and expiration_date < created_date:
            raise ValidationError('Expiration date is before creation date')
        elif last_checked_date and last_checked_date < created_date:
            raise ValidationError(f'Last checked date is before creation date')

    id = fields.UUID()
    tenant = fields.UUID()
    quota = fields.Int()
    created_date = fields.DateTime()
    expiration_date = fields.DateTime()
    last_checked_date = fields.DateTime()

    @post_load()
    def _make(self, data, **kwargs):
        return License(**data)
