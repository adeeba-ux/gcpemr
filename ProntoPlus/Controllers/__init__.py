from .patient_ctrl import PatientCtrl
from .record_ctrl import RecordCtrl
from .user_ctrl import UserCtrl
import ProntoPlus.Models.db as _db


def init_patient_ctrl():
    return PatientCtrl(_db.session)


def init_record_ctrl():
    return RecordCtrl(_db.session)


def init_user_ctrl():
    return UserCtrl(_db.session)
