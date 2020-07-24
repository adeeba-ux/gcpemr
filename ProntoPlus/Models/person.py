from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import date, datetime
from marshmallow import Schema, fields, post_load, ValidationError, validates_schema
from enum import Enum, unique

from ProntoPlus.Models._custom_fields import CPF, EnumField



@dataclass
class Person:
    """
    Classe base para objetos que representam pessoas.
    """

    @unique
    class Gender(Enum):
        undefined = -1
        masculine = 0
        feminine = 1
        other = 2

    @unique
    class BloodType(Enum):
        undefined = -1
        o = 0
        a = 1
        b = 2
        ab = 3

    @unique
    class BloodRH(Enum):
        undefined = -1
        negative = 0
        positive = 1

    tenant: UUID
    cpf: str
    name: str
    gender: Gender
    created_date: datetime = datetime.now()
    id: UUID = None
    birth_date: date = None
    address: str = None
    email: str = None
    blood_type: BloodType = BloodType(-1)
    blood_rh: BloodRH = BloodRH(-1)
    last_modified_date: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid4()
        if self.last_modified_date is None:
            self.last_modified_date = self.created_date


class PersonSchema(Schema):
    @validates_schema
    def must_be_higher_than_creation(self, data, **kwargs):
        created_date = data.get('created_date', None)
        if created_date is None:
            created_date = datetime.now()
        last_modified_date = data.get('last_modified_date', None)

        if last_modified_date and last_modified_date < created_date:
            raise ValidationError(f'Last modified date is before creation date')

    id = fields.UUID()
    tenant = fields.UUID()
    name = fields.Str()
    cpf = CPF()
    birth_date = fields.Date()
    gender = EnumField(Person.Gender)
    address = fields.Str()
    email = fields.Email()
    blood_type = EnumField(Person.BloodType)
    blood_rh = EnumField(Person.BloodRH)
    created_date = fields.DateTime()
    last_modified_date = fields.DateTime()

    @post_load
    def _make(self, data, **kwargs):
        return Person(**data)
