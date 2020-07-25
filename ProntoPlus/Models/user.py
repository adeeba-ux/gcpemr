import ProntoPlus.Models._db as db
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as sau
import dataclasses as da
import marshmallow as mw
import uuid
import datetime as dt
import passlib.hash as plib


@da.dataclass
class User:
    id_tenant: uuid.UUID
    id: uuid.UUID = da.field(default_factory=lambda: uuid.uuid4())
    id_person: uuid.UUID = da.field(default_factory=lambda: uuid.uuid4())
    crm: str = da.field(default_factory=lambda: None)
    username: str = da.field(default_factory=lambda: None)
    password: str = da.field(default_factory=lambda: None)
    created_date: dt.datetime = da.field(default_factory=lambda: dt.datetime.now())
    last_modified_date: dt.datetime = da.field(default_factory=lambda: None)

    def __post_init__(self):
        if self.last_modified_date is None:
            self.last_modified_date = self.created_date

        self.password = plib.bcrypt.encrypt(self.password)


class UserSchema(mw.Schema):
    @mw.validates_schema
    def _must_not_be_blank(self, data, **kwargs):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise mw.ValidationError(f'Username cannot be empty.')

        if password is None:
            raise mw.ValidationError(f'Password cannot be empty.')

    @mw.validates_schema
    def must_be_higher_than_creation(self, data, **kwargs):
        created_date = data.get('created_date', None)
        if created_date is None:
            created_date = dt.datetime.now()
        last_modified_date = data.get('last_modified_date', None)

        if last_modified_date and last_modified_date < created_date:
            raise mw.ValidationError(f'Last modified date is before creation date')

    id_person = mw.fields.UUID()
    crm = mw.fields.Str(allow_none=False)
    username = mw.fields.Str(required=True, allow_none=False)
    password = mw.fields.Str(load_only=True, required=True, allow_none=False)
    created_date = mw.fields.DateTime(required=True)
    last_modified_date = mw.fields.DateTime(allow_none=True)

    @mw.post_load
    def _make(self, data, **kwargs):
        return User(**data)


userTable = sa.Table(
    "users",
    db.Model.metadata,
    sa.Column('id', sau.UUIDType, primary_key=True, unique=True, nullable=False),
    sa.Column('id_person', sau.UUIDType, sa.ForeignKey('people.id')),
    sa.Column('crm', sa.String),
    sa.Column('username', sa.String, nullable=False),
    sa.Column('password', sa.String, nullable=False),
    sa.Column('created_date', sa.DateTime),
    sa.Column('last_modified_date', sa.DateTime)
)

orm.mapper(User, userTable)
