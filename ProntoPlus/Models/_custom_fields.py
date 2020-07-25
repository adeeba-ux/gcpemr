import marshmallow as mw
import enum
import typing as t


class EnumField(mw.fields.Field):

    def __init__(self, enum_class) -> None:
        super().__init__()
        self.enum_class = enum_class

    def _deserialize(self, value: t.Any, *args, **kwargs) -> enum.Enum:
        if not isinstance(value, self.enum_class):
            try:
                enum_value = self.enum_class(value)
            except ValueError:
                raise mw.ValidationError(f"Invalid {self.enum_class} value.")
        else:
            enum_value = value

        return enum_value

    def _serialize(self, value: enum.Enum, *args, **kwargs) -> t.Any:
        if value:
            return value.value
        else:
            return None


class CPF(mw.fields.Field):
    """CPF formatting field for Marshmallow."""

    def _deserialize(self, value: str, *args, **kwargs) -> str:
        value = value.replace('.', '').replace('-', '')

        if len(value) > 11:
            raise mw.ValidationError("Invalid CPF provided.")
        else:
            for n in value:
                try:
                    int(n)
                except ValueError:
                    raise mw.ValidationError("Invalid CPF provided.")

        return str(value)

    def _serialize(self, value: str, *args, **kwargs) -> str:
        return f'{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}'
