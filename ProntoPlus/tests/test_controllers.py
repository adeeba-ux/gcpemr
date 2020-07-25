import pytest
from ProntoPlus.Controllers import *
from ProntoPlus.tests._cases import *


def test_patientctrl_implementation():
    test_controller = PatientCtrl(test_mode=True)
    test_generator = Cases()
    cases = test_generator._make_patient_test_cases()
    schema = cases['schema']
    users = schema.load(cases['cases'], many=True)

    test_controller.add_patient(users, many=True)
    test_controller.get_patient(users[0].id)
    ids = []
    for u in users:
        ids.appent(u.id)

    test_controller.get_patient(ids, many=True)

    users[0].cpf = '12345678912'

    test_controller.update_patient(users[0])

    test_controller.delete_patient(users[1])
    test_controller.get_patient(users[1].id)

