import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as Models

import typing as t
import uuid
import datetime as dt
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')


class RecordCtrl(_base.BaseCtrl):
    CTRLCLASS = Models.Record
    _CTRLTYPE = t.Union[CTRLCLASS, t.List[CTRLCLASS]]
    _CTRLSCHEMA = Models.RecordSchema()

    def get_from_patient(self, patient_id, tenant_id):
        result = self._session.query(self.CTRLCLASS).filter(self.CTRLCLASS.id_patient == patient_id,
                                                            self.CTRLCLASS.tenant == tenant_id).all()
        if isinstance(result, list) and len(result) > 0:
            result = result[0]
        else:
            record = {
                'id': uuid.uuid4(),
                'id_user': uuid.uuid4(),
                'id_patient': patient_id,
                'tenant': tenant_id,
                'created_date': dt.datetime.now().strftime(cfg['CLIENT']['dateformat']),
                'text': ''
            }
            result = self.load(record)

        return result