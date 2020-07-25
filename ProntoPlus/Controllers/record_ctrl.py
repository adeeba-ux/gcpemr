import ProntoPlus.Controllers.base_ctrl as _base
import ProntoPlus.Models as models
import typing as t


class RecordCtrl(_base.BaseCtrl):
    _CTRLCLASS = models.Record
    _CTRLTYPE = t.Union[_CTRLCLASS, t.List[_CTRLCLASS]]


