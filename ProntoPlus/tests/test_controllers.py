import pytest
from ProntoPlus.Controllers import *
from ProntoPlus.tests._cases import *

def test_patientctrl_implementation():
    test_case = PatientCtrl(test_mode=True)
    test_generator = Cases()

