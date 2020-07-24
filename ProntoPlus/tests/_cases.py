from uuid import uuid4
from datetime import datetime, timedelta
from ProntoPlus.Models import *


# Input generators
class Cases:
    TENANT = uuid4()
    SCHEMAS = {
        'person': PersonSchema,
        'user': UserSchema,
        'patient': PatientSchema,
        'record': RecordSchema,
        'license': LicenseSchema
    }
    CLASSES = {
        'person': Person,
        'user': User,
        'patient': Patient,
        'record': Record,
        'license': License
    }

    def __init__(self):
        self.test_cases = [self._make_person_test_cases, self._make_user_test_cases, self._make_patient_test_cases,
                           self._make_record_test_cases, self._make_license_test_cases]

    def _make_person_test_cases(self):
        return {
            'cases': [
                {
                    "tenant": self.TENANT,
                    "cpf": "12345678910",
                    "name": "Test User",
                    "gender": Person.Gender.masculine,
                    "birth_date": '2020-12-10',
                    "address": 'Test Street, 1',
                    "email": "test.email@email.com",
                    "blood_type": Person.BloodType.ab,
                    "blood_rh": Person.BloodRH.negative,
                    "created_date": datetime.now().isoformat()
                },
                {
                    "tenant": self.TENANT,
                    "cpf": "12345678911",
                    "name": "Test User 2",
                    "gender": Person.Gender.feminine,
                    "birth_date": '1984-12-01',
                    "address": 'Test Street, 2',
                    "email": "test.email.2@email.com",
                    "blood_type": Person.BloodType.o,
                    "blood_rh": Person.BloodRH.undefined,
                    "created_date": datetime.now().isoformat()
                },
                {
                    "tenant": self.TENANT,
                    "cpf": "12345678910",
                    "name": "Test User",
                    "gender": Person.Gender.masculine,
                    "birth_date": '1988-01-01',
                    "address": 'Test Street, 2',
                    "email": "testemail@email.com",
                    "blood_type": Person.BloodType.undefined,
                    "blood_rh": Person.BloodRH.undefined,
                    "created_date": datetime.now().isoformat()
                }
            ],
            'schema': self.SCHEMAS['person'],
            'class': self.CLASSES['person']
        }

    def _make_user_test_cases(self):
        user_test_cases = self._make_person_test_cases()
        user_test_cases['schema'] = self.SCHEMAS['user']
        user_test_cases['class'] = self.CLASSES['user']

        for i, case in enumerate(user_test_cases['cases']):
            if i == 0:
                case['crm'] = '114991'
            if i == 2:
                case['crm'] = '06/143550'
            else:
                case['crm'] = ''

            case['username'] = 'user' + str(i)
            case['password'] = 'password' + str(i)

            user_test_cases['cases'][i] = case

        return user_test_cases

    def _make_patient_test_cases(self):
        patient_test_cases = self._make_person_test_cases()
        patient_test_cases['schema'] = self.SCHEMAS['patient']

        return patient_test_cases

    def _make_test_user(self):
        user_case = self._make_user_test_cases()
        test_user = user_case['schema']().load(user_case['cases'][0])
        return test_user

    def _make_test_patient(self):
        patient_case = self._make_patient_test_cases()
        test_patient = patient_case['schema']().load(patient_case['cases'][0])
        return test_patient

    def _make_record_test_cases(self):
        test_user = self._make_test_user()
        test_patient = self._make_test_patient()

        record_cases = [
            {
                'id_user': test_user.id,
                'id_tenant': self.TENANT,
                'id_patient': test_patient.id,
                'text': 'Test Medical Record',
                'created_date': datetime.now().isoformat()
            },
            {
                'id_user': test_user.id,
                'id_tenant': self.TENANT,
                'id_patient': test_patient.id,
                'text': 'Test Medical Record',
                'created_date': datetime(2020, 1, 1, 15, 50, 50).isoformat()
            }
        ]

        return {'cases': record_cases, 'schema': self.SCHEMAS['record'], 'class': self.CLASSES['record'],
                'test_user': test_user, 'test_patient': test_patient}

    def _make_license_test_cases(self):
        return {
            'cases': [
                {
                    'id': uuid4(),
                    'tenant': uuid4(),
                    'quota': 10,
                    'created_date': datetime.now().isoformat()
                },
                {
                    'id': uuid4(),
                    'tenant': uuid4(),
                    'quota': 9,
                    'created_date': datetime.now().isoformat(),
                    'expiration_date': (datetime.now() + timedelta(days=1)).isoformat(),
                    'last_checked_date': datetime.now().isoformat()
                }
            ],
            'schema': self.SCHEMAS['license'],
            'class': self.CLASSES['license']
        }


class BadCases(Cases):

    def __init__(self):
        self.test_cases = [self._make_bad_person_test_cases, self._make_bad_user_test_cases,
                           self._make_bad_patient_test_cases, self._make_bad_record_test_cases,
                           self._make_bad_license_test_cases]

    def _make_bad_person_test_cases(self):
        bad_test_cases = self._make_person_test_cases()
        bad_test_cases2 = self._make_person_test_cases()

        for i, case in enumerate(bad_test_cases['cases']):
            if i == 0:
                case['blood_type'] = '-1'
            if i == 1:
                case['blood_rh'] = '-1'
            if i == 2:
                case['gender'] = '-1'
            else:
                case['email'] = case['email'].replace('@', '')

            bad_test_cases['cases'][i] = case

        for i, case in enumerate(bad_test_cases2['cases']):
            if i == 0:
                case['blood_type'] = 'o'
            if i == 1:
                case['blood_rh'] = 'negative'
            if i == 2:
                case['gender'] = 'masculine'
            else:
                case['email'] = 'NA'

            bad_test_cases2['cases'][i] = case

        return {
            'cases': [
                bad_test_cases['cases'],
                bad_test_cases2['cases']
            ],
            'schema': bad_test_cases['schema'],
            'class': self.CLASSES['person']
        }

    def _make_bad_user_test_cases(self):
        bad_user_cases = self._make_user_test_cases()

        for i, case in enumerate(bad_user_cases['cases']):
            if i == 0:
                case['crm'] = None
            if i == 1:
                case['password'] = None
            if i == 2:
                case['username'] = None

        return bad_user_cases

    def _make_bad_patient_test_cases(self):
        bad_test_cases = self._make_bad_person_test_cases()
        bad_test_cases['schema'] = self.SCHEMAS['patient']
        bad_test_cases['class'] = self.CLASSES['patient']

        return bad_test_cases

    def _make_bad_record_test_cases(self):
        bad_record_cases = self._make_record_test_cases()
        bad_record_cases['cases'].append(bad_record_cases['cases'][0].copy())

        for i, case in enumerate(bad_record_cases['cases']):
            if i == 0:
                case['id_user'] = 'User1'
            if i == 1:
                case['id_patient'] = 'Patient1'
            else:
                case['created_date'] = '2020-01-01 00:00:00'
            bad_record_cases['cases'][i] = case

        return {'cases': bad_record_cases['cases'], 'schema': bad_record_cases['schema'],
                'class': self.CLASSES['record']}

    def _make_bad_license_test_cases(self):
        bad_license_cases = self._make_license_test_cases()
        bad_license_cases['cases'] += [bad_license_cases['cases'][0].copy()] * 3

        for i, case in enumerate(bad_license_cases['cases']):
            if i == 0:
                case['id'] = 'Key1'
            elif i == 1:
                case['created_date'] = datetime(2020, 20, 1)
            elif i == 2:
                case['expiration_date'] = datetime(2020, 20, 1, 10, 55).isoformat()
                case['created_date'] = datetime(2020, 20, 1, 10, 54).isoformat()
            elif i == 3:
                case['quota'] = -1
            elif i == 4:
                case['last_checked_date'] = datetime(2020, 20, 1)

            bad_license_cases['cases'][i] = case

            return bad_license_cases
