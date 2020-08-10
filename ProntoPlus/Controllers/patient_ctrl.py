import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Controllers.record_ctrl as _record
import ProntoPlus.Models as Models
import typing as t


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

    def delete(self, obj: _CTRLTYPE, many: bool = False) -> t.Union[bool, t.List[t.Union[Exception]]]:
        _rec_ctrl = _record.RecordCtrl(self._session)

        if many:
            if not isinstance(obj, list):
                obj = [obj]
            try:
                for o in obj:
                    self._session.query(_rec_ctrl.CTRLCLASS).filter(
                        _rec_ctrl.CTRLCLASS.id_patient == o.id, _rec_ctrl.CTRLCLASS.tenant == o.tenant).delete()

                    self._session.query(self.CTRLCLASS).filter(self.CTRLCLASS.id == o.id).delete()
            except Exception as e:
                return [False, e]
        else:
            try:
                self._session.query(_rec_ctrl.CTRLCLASS).filter(
                    _rec_ctrl.CTRLCLASS.id_patient == obj.id, _rec_ctrl.CTRLCLASS.tenant == obj.tenant).delete()

                self._session.query(self.CTRLCLASS).filter(self.CTRLCLASS.id == obj.id).delete()
            except Exception as e:
                return [False, e]

        self._session.commit()
        return True
