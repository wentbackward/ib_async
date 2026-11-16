from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AttachedOrders(_message.Message):
    __slots__ = ("slOrderId", "slOrderType", "ptOrderId", "ptOrderType")
    SLORDERID_FIELD_NUMBER: _ClassVar[int]
    SLORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    PTORDERID_FIELD_NUMBER: _ClassVar[int]
    PTORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    slOrderId: int
    slOrderType: str
    ptOrderId: int
    ptOrderType: str
    def __init__(self, slOrderId: _Optional[int] = ..., slOrderType: _Optional[str] = ..., ptOrderId: _Optional[int] = ..., ptOrderType: _Optional[str] = ...) -> None: ...
