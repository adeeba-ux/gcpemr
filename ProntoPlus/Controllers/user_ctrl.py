import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as models
import typing as t
import passlib.hash as plib
import uuid
import operator


class UserCtrl(_base.BaseCtrl):
    _CTRLCLASS = models.User
    _CTRLTYPE = t.Union[_CTRLCLASS, t.List[_CTRLCLASS]]

    def verify(self, tenant_id: uuid.UUID, obj: _CTRLTYPE) -> bool:
        valid = self._session.query(self._CTRLCLASS).filter(self._CTRLCLASS.username == obj.username,
                                                            self._CTRLCLASS.id_tenant == tenant_id).all()

        # if more than one username in the database for some reason,
        # it will select the highest created_date
        if len(valid) > 1:
            valid = max(valid, key=operator.attrgetter('created_date'))

        return plib.bcrypt.verify(obj.password, valid.password)
