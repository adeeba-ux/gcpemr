import pytest


def test_patient_ctrl_implementation(patient_controller, case_generator):
    cases_repo = case_generator.make_patient_test_cases()
    schema = cases_repo['schema']()
    patients = schema.load(cases_repo['cases'], many=True)

    # add many
    assert patient_controller.add(patients, many=True) is True

    # get all
    all_patients = patient_controller.get_all().all()
    assert len(all_patients) == len(patients)

    # update one
    old_cpf = patients[0].cpf
    patients[0].cpf = '12345678913'
    assert patient_controller.add(patients[0]) is True

    # get one
    get_patient = patient_controller.get_one(patients[0].id).all()
    assert get_patient[0].id == patients[0].id
    assert get_patient[0].cpf != old_cpf







