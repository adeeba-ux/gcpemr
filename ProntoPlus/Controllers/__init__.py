from .patient_ctrl import PatientCtrl
from .record_ctrl import RecordCtrl
from .user_ctrl import UserCtrl
import ProntoPlus.db as _db

engine = _db.make_engine()
session = _db.make_session(engine)

def init_patient_ctrl() -> PatientCtrl:
    return PatientCtrl(session)


def init_record_ctrl() -> RecordCtrl:
    return RecordCtrl(session)


def init_user_ctrl() -> UserCtrl:
    return UserCtrl(session)
