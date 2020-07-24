from ProntoPlus.Models import Person, PersonSchema
from marshmallow import post_load


class Patient(Person):
    pass


class PatientSchema(PersonSchema):

    @post_load
    def _make(self, data, **kwargs):
        return Patient(**data)
