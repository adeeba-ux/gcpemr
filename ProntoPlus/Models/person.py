import dataclasses as da
import uuid
import datetime as dt
import enum
import marshmallow as mw
import ProntoPlus.Models._custom_fields as _custom_fields
import ProntoPlus.Models.base_model as _base
import abc

@da.dataclass
class Person(_base.Base, abc.ABC):
    """
    Base class for objects that represent a Person.
    """

    @enum.unique
    class Gender(enum.Enum):
        undefined = -1
        masculine = 0
        feminine = 1
        other = 2

    @enum.unique
    class BloodType(enum.Enum):
        undefined = -1
        o = 0
        a = 1
        b = 2
        ab = 3

    @enum.unique
    class BloodRH(enum.Enum):
        undefined = -1
        negative = 0
        positive = 1

    cpf: str = da.field(default_factory=lambda: None)
    name: str = da.field(default_factory=lambda: '')
    gender: Gender = da.field(default_factory=lambda: Person.Gender(-1))
    created_date: dt.datetime = da.field(default_factory=lambda: dt.datetime.now())
    birth_date: dt.date = da.field(default_factory=lambda: None)
    address: str = da.field(default_factory=lambda: None)
    email: str = da.field(default_factory=lambda: None)
    phone: str = da.field(default_factory=lambda: None)
    blood_type: BloodType = da.field(default_factory=lambda: Person.BloodType(-1))
    blood_rh: BloodRH = da.field(default_factory=lambda: Person.BloodRH(-1))
    last_modified_date: dt.datetime = da.field(default_factory=lambda: None)

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()
        if self.last_modified_date is None:
            self.last_modified_date = self.created_date


class PersonSchema(mw.Schema):
    @mw.validates_schema
    def must_be_higher_than_creation(self, data, **kwargs):
        created_date = data.get('created_date', None)
        if created_date is None:
            created_date = dt.datetime.now()
        last_modified_date = data.get('last_modified_date', None)

        if last_modified_date and last_modified_date < created_date:
            raise mw.ValidationError(f'Last modified date is before creation date')

    name = mw.fields.Str(required=True, allow_none=False)
    cpf = _custom_fields.CPF(required=True, allow_none=False)
    birth_date = mw.fields.Date()
    gender = _custom_fields.EnumField(Person.Gender)
    address = mw.fields.Str()
    email = mw.fields.Email()
    phone = mw.fields.Str()
    blood_type = _custom_fields.EnumField(Person.BloodType)
    blood_rh = _custom_fields.EnumField(Person.BloodRH)
    created_date = mw.fields.DateTime(required=True)
    last_modified_date = mw.fields.DateTime()

    @mw.post_load
    def _make(self, data, **kwargs):
        return Person(**data)
