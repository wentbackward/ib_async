from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LockAndExitConfig(_message.Message):
    __slots__ = ("autoLogoffTime", "autoLogoffPeriod", "autoLogoffType")
    AUTOLOGOFFTIME_FIELD_NUMBER: _ClassVar[int]
    AUTOLOGOFFPERIOD_FIELD_NUMBER: _ClassVar[int]
    AUTOLOGOFFTYPE_FIELD_NUMBER: _ClassVar[int]
    autoLogoffTime: str
    autoLogoffPeriod: str
    autoLogoffType: str
    def __init__(self, autoLogoffTime: _Optional[str] = ..., autoLogoffPeriod: _Optional[str] = ..., autoLogoffType: _Optional[str] = ...) -> None: ...
