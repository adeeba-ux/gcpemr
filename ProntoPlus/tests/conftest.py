import pytest
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ProntoPlus.Controllers as Ctrls
import ProntoPlus.db as _db

from ProntoPlus.tests._cases import *


@pytest.fixture(scope='session')
def engine_mocker():
    return sa.create_engine('sqlite://')


@pytest.fixture(scope='session')
def session_mocker(engine_mocker):
    engine = engine_mocker
    _db.metadata.create_all(engine)
    session = orm.sessionmaker(engine)()

    return session


@pytest.fixture
def case_generator():
    generator = Cases()

    return generator


@pytest.fixture
def bad_case_generator():
    generator = BadCases()

    return generator


@pytest.fixture
def patient_controller(session_mocker):
    controller = Ctrls.PatientCtrl(session_mocker)
    return controller


@pytest.fixture
def user_controller(session_mocker):
    controller = Ctrls.UserCtrl(session_mocker)
    return controller


@pytest.fixture
def record_controller(session_mocker):
    controller = Ctrls.RecordCtrl(session_mocker)
    return controller





