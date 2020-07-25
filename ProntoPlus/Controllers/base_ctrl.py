import ProntoPlus.Models.base_model as _base
import uuid
import typing as t
import sqlalchemy.orm as orm
import abc


class BaseCtrl(abc.ABC):
    _CTRLCLASS: _base.Base = _base.Base
    _CTRLTYPE = t.Union[_CTRLCLASS, t.List[_CTRLCLASS]]

    def __init__(self, session: orm.Session) -> None:
        self._session = session

    def get(self, obj_id: t.Union[uuid.UUID, t.List[uuid.UUID]],
            many: bool = False) -> _CTRLTYPE:

        if many:
            if not isinstance(obj_id, list):
                obj_id = [obj_id]
            result = self._session.query(obj_id).filter(self._CTRLCLASS.id.in_(obj_id)).all()
        else:
            result = self._session.query(obj_id).filter(self._CTRLCLASS.id == obj_id).all()

        return result

    def add(self, obj: _CTRLTYPE, many: bool = False) -> t.Union[bool, t.List[bool, Exception]]:
        if many:
            if not isinstance(obj, list):
                obj = [obj]
            try:
                self._session.add_all(obj)
            except Exception as e:
                return [False, e]
        else:
            try:
                self._session.add(obj)
            except Exception as e:
                return [False, e]

        self._session.commit()
        return True

    def delete(self, obj: _CTRLTYPE, many: bool = False) -> t.Union[bool, t.List[bool, Exception]]:
        if many:
            if not isinstance(obj, list):
                obj = [obj]
            try:
                for o in obj:
                    self._session.query(obj).filter(self._CTRLCLASS.id == o.id).delete()
            except Exception as e:
                return [False, e]
        else:
            try:
                self._session.query(obj).filter(self._CTRLCLASS.id == obj.id).delete()
            except Exception as e:
                return [False, e]

        self._session.commit()
        return True
