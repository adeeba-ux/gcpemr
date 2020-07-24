from ProntoPlus.Models import Person, PersonSchema
from dataclasses import dataclass
from marshmallow import fields, post_load, ValidationError


# Helper validation function
def _must_not_be_blank(data):
    if not data:
        raise ValidationError(f'Not provided.')


@dataclass
class User(Person):
    crm: str = None
    username: str = None
    password: str = None


class UserSchema(PersonSchema):
    crm = fields.Str()
    username = fields.Str(validate=_must_not_be_blank)
    password = fields.Str(load_only=True, validate=_must_not_be_blank)

    @post_load
    def _make(self, data, **kwargs):
        return User(**data)
