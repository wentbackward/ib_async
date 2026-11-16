from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TickReqParams(_message.Message):
    __slots__ = ("reqId", "minTick", "bboExchange", "snapshotPermissions", "lastPricePrecision", "lastSizePrecision")
    REQID_FIELD_NUMBER: _ClassVar[int]
    MINTICK_FIELD_NUMBER: _ClassVar[int]
    BBOEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    LASTPRICEPRECISION_FIELD_NUMBER: _ClassVar[int]
    LASTSIZEPRECISION_FIELD_NUMBER: _ClassVar[int]
    reqId: int
    minTick: str
    bboExchange: str
    snapshotPermissions: int
    lastPricePrecision: str
    lastSizePrecision: str
    def __init__(self, reqId: _Optional[int] = ..., minTick: _Optional[str] = ..., bboExchange: _Optional[str] = ..., snapshotPermissions: _Optional[int] = ..., lastPricePrecision: _Optional[str] = ..., lastSizePrecision: _Optional[str] = ...) -> None: ...
