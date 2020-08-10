import pytest
import sqlalchemy.orm as orm


def _make_cases(cases_repo):
    schema = cases_repo['schema']()
    generated_cases = schema.load(cases_repo['cases'], many=True)

    return generated_cases


def test_patient_ctrl_implementation(patient_controller, case_generator):
    patients = _make_cases(case_generator.make_patient_test_cases())

    # add many
    assert patient_controller.add(patients, many=True) is True

    # get all
    all_patients = patient_controller.get_all().all()
    assert len(all_patients) == len(patients)

    # update one
    patients[0].cpf = '12345678913'
    assert patient_controller.add(patients[0]) is True

    # get one
    get_patient = patient_controller.get(patients[0].id).all()
    assert get_patient[0].name == patients[0].name
    assert get_patient[0].cpf == patients[0].cpf

    # get many
    patient_ids = []
    for p in patients:
        patient_ids.append(p.id)

    get_patients = patient_controller.get(patient_ids, many=True).all()
    assert len(get_patients) == len(patient_ids)


def test_user_ctrl_implementation(user_controller, case_generator):
    users = _make_cases(case_generator.make_user_test_cases())

    # add many
    assert user_controller.add(users, many=True) is True

    # get all
    all_users = user_controller.get_all().all()
    assert len(all_users) == len(users)

    # update one
    users[0].password = '1234567'
    assert user_controller.add(users[0]) is True

    # get one
    get_user = user_controller.get(users[0].id).all()
    assert get_user[0].username == users[0].username
    assert get_user[0].password == users[0].password

    # verify method
    assert user_controller.verify(users[0].username, users[0].password, users[0].tenant)


def test_record_ctrl_implementation(record_controller, case_generator):
    records = _make_cases(case_generator.make_record_test_cases())

    # add many
    assert record_controller.add(records, many=True) is True

    # get all
    all_records = record_controller.get_all().all()
    assert len(all_records) == len(records)

    # update one
    records[0].text = 'Lorem Ipsum Two'
    assert record_controller.add(records[0]) is True

    # get one
    get_record = record_controller.get(records[0].id).all()
    # assert get_record[0].id_user == records[0].id_user
    assert get_record[0].text == records[0].text







