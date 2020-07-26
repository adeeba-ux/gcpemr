import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as models
import typing as t
import passlib.hash as plib
import uuid
import operator


class UserCtrl(_base.BaseCtrl):
    _CTRLCLASS = models.User
    _CTRLTYPE = t.Union[_CTRLCLASS, t.List[_CTRLCLASS]]

    def verify(self, username: str, password: str, tenant_id: uuid.UUID) -> bool:
        valid = self._session.query(self._CTRLCLASS).filter(self._CTRLCLASS.username == username,
                                                            self._CTRLCLASS.tenant == tenant_id).all()

        # if more than one username in the database for some reason,
        # it will select the highest created_date
        if len(valid) > 1:
            valid = max(valid, key=operator.attrgetter('created_date'))

        return password == valid[0].password
