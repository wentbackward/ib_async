from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateConfigWarning(_message.Message):
    __slots__ = ("messageId", "title", "message")
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    messageId: int
    title: str
    message: str
    def __init__(self, messageId: _Optional[int] = ..., title: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
