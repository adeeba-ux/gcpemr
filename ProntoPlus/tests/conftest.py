import pytest
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ProntoPlus.Models.db as db
import ProntoPlus.Controllers as ctrls

from ProntoPlus.tests._cases import *


@pytest.fixture(scope='session')
def session_mocker():
    engine = sa.create_engine('sqlite://')
    db.metadata.create_all(engine)

    session = orm.sessionmaker(engine)()

    return session


@pytest.fixture
def controllers(session_mocker):
    def patient_controller():
        controller = ctrls.PatientCtrl(session_mocker)
        return controller

    def user_controller():
        controller = ctrls.UserCtrl(session_mocker)
        return controller

    def record_controller():
        controller = ctrls.RecordCtrl(session_mocker)
        return controller

    return [patient_controller(), user_controller(), record_controller()]


@pytest.fixture
def case_generator():
    generator = Cases()

    return generator


@pytest.fixture
def bad_case_generator():
    generator = BadCases()

    return generator


