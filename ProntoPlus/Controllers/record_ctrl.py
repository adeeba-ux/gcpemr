import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as Models
import typing as t


class RecordCtrl(_base.BaseCtrl):
    CTRLCLASS = Models.Record
    _CTRLTYPE = t.Union[CTRLCLASS, t.List[CTRLCLASS]]
    _CTRLSCHEMA = Models.RecordSchema()


