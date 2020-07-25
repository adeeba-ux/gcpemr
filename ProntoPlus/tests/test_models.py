import pytest
import marshmallow as mw
import uuid


from ProntoPlus.tests._cases import *


def test_models_implementations():
    cases_generator = Cases()

    for test_case_maker in cases_generator.test_cases:
        cases_repo = test_case_maker()

        schema = cases_repo['schema']()

        if len(cases_repo['cases']) > 1:
            results = schema.load(cases_repo['cases'], many=True)
        else:
            results = [schema.load(cases_repo['cases'])]

        for r in results:
            assert isinstance(r, cases_repo['class'])
            assert isinstance(r.id, uuid.UUID)

            if cases_repo['class'] == cases_generator.CLASSES['user']:
                assert schema.dump(r).get('password') is None

            if cases_repo['class'] == cases_generator.CLASSES['record']:
                assert r.id_user == cases_repo['test_user'].id
                assert r.id_patient == cases_repo['test_patient'].id

                assert r.last_modified_date == r.created_date


def test_validations():
    cases_generator = BadCases()

    for test_case_maker in cases_generator.test_cases:
        cases_repo = test_case_maker()
        schema = cases_repo['schema']()

        for test_case in cases_repo['cases']:
            for case in test_case:
                with pytest.raises(mw.ValidationError) as e_info:
                    schema.load(case)


def test_database_integration():
    pass