import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as Models
import typing as t


class PatientCtrl(_base.BaseCtrl):
    CTRLCLASS = Models.Patient
    _CTRLTYPE = t.Union[CTRLCLASS, t.List[CTRLCLASS]]
    _CTRLSCHEMA = Models.PatientSchema()
