import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as Models
import typing as t
import uuid
import operator


class UserCtrl(_base.BaseCtrl):
    CTRLCLASS = Models.User
    _CTRLTYPE = t.Union[CTRLCLASS, t.List[CTRLCLASS]]
    _CTRLSCHEMA = Models.UserSchema()

    def verify(self, username: str, password: str, tenant_id: uuid.UUID) -> bool:
        valid = self._session.query(self.CTRLCLASS).filter(self.CTRLCLASS.username == username,
                                                           self.CTRLCLASS.tenant == tenant_id).all()

        # if more than one username in the database for some reason,
        # it will select the highest created_date
        if len(valid) > 1:
            valid = max(valid, key=operator.attrgetter('created_date'))

        return password == valid[0].password
