import marshmallow as mw
import dataclasses as da
import datetime as dt
import ProntoPlus.Models.base as _base


@da.dataclass()
class License(_base.Base):
    quota: int = da.field(default_factory=lambda: 1)
    created_date: dt.datetime = da.field(default_factory=lambda: dt.datetime.now())
    expiration_date: dt.datetime = da.field(default_factory=lambda: None)
    last_checked_date: dt.datetime = da.field(default_factory=lambda: None)

    def __post_init__(self):
        if self.last_checked_date is None:
            self.last_checked_date = self.created_date


class LicenseSchema(mw.Schema):
    @mw.validates("quota")
    def must_be_at_least_one(self, data):
        if isinstance(data, int) and data < 1:
            raise mw.ValidationError('Quota must be 1 or more.')

    @mw.validates_schema
    def must_be_higher_than_creation(self, data, **kwargs):
        created_date = data.get('created_date', None)
        if created_date is None:
            created_date = dt.datetime.now()
        
        expiration_date = data.get('expiration_date', None)
        last_checked_date = data.get('last_checked_date', None)

        if expiration_date and expiration_date < created_date:
            raise mw.ValidationError('Expiration date is before creation date')
        elif last_checked_date and last_checked_date < created_date:
            raise mw.ValidationError(f'Last checked date is before creation date')

    quota = mw.fields.Int(required=True)
    created_date = mw.fields.DateTime(required=True)
    expiration_date = mw.fields.DateTime(allow_none=True)
    last_checked_date = mw.fields.DateTime(allow_none=True)

    @mw.post_load()
    def _make(self, data, **kwargs):
        return License(**data)
