from . import UpdateConfigWarning_pb2 as _UpdateConfigWarning_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateConfigResponse(_message.Message):
    __slots__ = ("reqId", "status", "message", "changedFields", "errors", "warnings")
    REQID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHANGEDFIELDS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    reqId: int
    status: str
    message: str
    changedFields: _containers.RepeatedScalarFieldContainer[str]
    errors: _containers.RepeatedScalarFieldContainer[str]
    warnings: _containers.RepeatedCompositeFieldContainer[_UpdateConfigWarning_pb2.UpdateConfigWarning]
    def __init__(self, reqId: _Optional[int] = ..., status: _Optional[str] = ..., message: _Optional[str] = ..., changedFields: _Optional[_Iterable[str]] = ..., errors: _Optional[_Iterable[str]] = ..., warnings: _Optional[_Iterable[_Union[_UpdateConfigWarning_pb2.UpdateConfigWarning, _Mapping]]] = ...) -> None: ...
