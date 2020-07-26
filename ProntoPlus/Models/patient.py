import ProntoPlus.Models as models
import ProntoPlus.Models.db as _db
import marshmallow as mw
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as sau
import datetime as dt


class Patient(models.Person):
    pass


class PatientSchema(models.PersonSchema):

    @mw.post_load
    def _make(self, data, **kwargs):
        return Patient(**data)


patientTable = sa.Table(
    "patients",
    _db.metadata,
    sa.Column('id', sau.UUIDType, primary_key=True, unique=True, nullable=False),
    sa.Column('tenant', sau.UUIDType, nullable=False),
    sa.Column('name', sa.String, nullable=False),
    sa.Column('cpf', sa.String, nullable=False),
    sa.Column('gender', sa.Enum(models.Person.Gender, values_callable=lambda x: [str(y.value) for y in x]),
              nullable=False, default=models.Person.Gender(-1)),
    sa.Column('birth_date', sa.DateTime),
    sa.Column('address', sa.String),
    sa.Column('email', sau.EmailType),
    sa.Column('phone', sau.PhoneNumberType),
    sa.Column('blood_type', sa.Enum(models.Person.BloodType, values_callable=lambda x: [str(y.value) for y in x]),
              default=models.Person.BloodType(-1)),
    sa.Column('blood_rh', sa.Enum(models.Person.BloodRH, values_callable=lambda x: [str(y.value) for y in x]),
              default=models.Person.BloodRH(-1)),
    sa.Column('created_date', sa.DateTime, nullable=False, default=dt.datetime.now),
    sa.Column('last_modified_date', sa.DateTime)
)

orm.mapper(Patient, patientTable)
