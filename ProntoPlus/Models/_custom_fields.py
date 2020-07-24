from marshmallow import fields, ValidationError


class EnumField(fields.Field):

    def __init__(self, enum_class):
        super().__init__()
        self.enum_class = enum_class

    def _deserialize(self, value, *args, **kwargs):
        if not isinstance(value, self.enum_class):
            raise ValidationError(f"Invalid {self.enum_class} object.")

        return value

    def _serialize(self, value, *args, **kwargs):
        return value


class CPF(fields.Field):
    """CPF formatting field for Marshmallow."""

    def _deserialize(self, value, *args, **kwargs):
        if len(value) > 11:
            raise ValidationError("Invalid CPF provided.")
        else:
            for n in value:
                try:
                    int(n)
                except ValueError:
                    raise ValidationError("Invalid CPF provided.")

        return str(value)

    def _serialize(self, value, *args, **kwargs):
        return f'{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}'
