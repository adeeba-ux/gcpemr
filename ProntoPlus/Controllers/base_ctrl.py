import ProntoPlus.Models.base as _base
import uuid
import typing as t
import sqlalchemy.orm as orm
import sqlalchemy as sa
import abc
import marshmallow as mw


class BaseCtrl(abc.ABC):
    CTRLCLASS: _base.Base = _base.Base
    _CTRLTYPE = t.Union[CTRLCLASS, t.List[CTRLCLASS]]
    _CTRLSCHEMA = mw.Schema = _base.BaseSchema()

    def __init__(self, session: orm.Session) -> None:
        self._session = session

    def get_all(self):
        return self._session.query(self.CTRLCLASS)

    def get(self, obj_id: t.Union[uuid.UUID, t.List[uuid.UUID]] = None,
            many: bool = False) -> _CTRLTYPE:

        if many:
            if not isinstance(obj_id, list):
                obj_id = [obj_id]
            result = self._session.query(self.CTRLCLASS).filter(self.CTRLCLASS.id.in_(obj_id))
        else:
            result = self._session.query(self.CTRLCLASS).filter(self.CTRLCLASS.id == obj_id)

        return result

    def _upsert(self, obj: _CTRLTYPE):
        check_if_exists = self.get(obj.id).all()
        if check_if_exists:
            self._session.merge(obj)
        else:
            self._session.add(obj)
        return True

    def add(self, obj: _CTRLTYPE, many: bool = False) -> t.Union[bool, t.List[t.Union[Exception]]]:

        if many:
            if not isinstance(obj, list):
                obj = [obj]
            try:
                for o in obj:
                    self._upsert(o)
            except Exception as e:
                return [False, e]
        else:
            try:
                self._upsert(obj)
            except Exception as e:
                return [False, e]

        self._session.commit()
        return True

    def delete(self, obj: _CTRLTYPE, many: bool = False) -> t.Union[bool, t.List[t.Union[Exception]]]:
        if many:
            if not isinstance(obj, list):
                obj = [obj]
            try:
                for o in obj:
                    self._session.query(obj).filter(self.CTRLCLASS.id == o.id).delete()
            except Exception as e:
                return [False, e]
        else:
            try:
                self._session.query(obj).filter(self.CTRLCLASS.id == obj.id).delete()
            except Exception as e:
                return [False, e]

        self._session.commit()
        return True

    def dump(self, obj, **kwargs):
        return self._CTRLSCHEMA.dump(obj=obj, **kwargs)

    def load(self, data, **kwargs):
        return self._CTRLSCHEMA.load(data=data, **kwargs)

    def presentation(self):
        return self.CTRLCLASS.presentation

