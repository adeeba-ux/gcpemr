import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as models
import typing as t
import uuid


class PatientCtrl(_base.BaseCtrl):
    _CTRLCLASS = models.Patient
    _CTRLTYPE = t.Union[_CTRLCLASS, t.List[_CTRLCLASS]]

    def get_records(self, obj_id: uuid.UUID) -> t.List[models.Record]:
        records = self._session.query(models.Record).filter(models.Record.id_patient == obj_id)

        return records
