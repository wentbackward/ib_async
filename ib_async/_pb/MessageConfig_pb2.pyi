from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageConfig(_message.Message):
    __slots__ = ("id", "title", "message", "defaultAction", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTACTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    message: str
    defaultAction: str
    enabled: bool
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., message: _Optional[str] = ..., defaultAction: _Optional[str] = ..., enabled: _Optional[bool] = ...) -> None: ...
