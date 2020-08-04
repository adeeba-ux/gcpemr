import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as Models
import typing as t
import uuid


class PatientCtrl(_base.BaseCtrl):
    CTRLCLASS = Models.Patient
    _CTRLTYPE = t.Union[CTRLCLASS, t.List[CTRLCLASS]]
    _CTRLSCHEMA = Models.PatientSchema()

    @staticmethod
    def gender_to_string(gender_nbr: int) -> str:
        genders = {
            -1: 'Não Definido',
            0: 'Masculino',
            1: 'Feminino'
        }

        return genders.get(gender_nbr)
