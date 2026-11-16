from . import LockAndExitConfig_pb2 as _LockAndExitConfig_pb2
from . import MessageConfig_pb2 as _MessageConfig_pb2
from . import ApiConfig_pb2 as _ApiConfig_pb2
from . import OrdersConfig_pb2 as _OrdersConfig_pb2
from . import UpdateConfigWarning_pb2 as _UpdateConfigWarning_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateConfigRequest(_message.Message):
    __slots__ = ("reqId", "lockAndExit", "messages", "api", "orders", "acceptedWarnings", "resetAPIOrderSequence")
    REQID_FIELD_NUMBER: _ClassVar[int]
    LOCKANDEXIT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTEDWARNINGS_FIELD_NUMBER: _ClassVar[int]
    RESETAPIORDERSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    reqId: int
    lockAndExit: _LockAndExitConfig_pb2.LockAndExitConfig
    messages: _containers.RepeatedCompositeFieldContainer[_MessageConfig_pb2.MessageConfig]
    api: _ApiConfig_pb2.ApiConfig
    orders: _OrdersConfig_pb2.OrdersConfig
    acceptedWarnings: _containers.RepeatedCompositeFieldContainer[_UpdateConfigWarning_pb2.UpdateConfigWarning]
    resetAPIOrderSequence: bool
    def __init__(self, reqId: _Optional[int] = ..., lockAndExit: _Optional[_Union[_LockAndExitConfig_pb2.LockAndExitConfig, _Mapping]] = ..., messages: _Optional[_Iterable[_Union[_MessageConfig_pb2.MessageConfig, _Mapping]]] = ..., api: _Optional[_Union[_ApiConfig_pb2.ApiConfig, _Mapping]] = ..., orders: _Optional[_Union[_OrdersConfig_pb2.OrdersConfig, _Mapping]] = ..., acceptedWarnings: _Optional[_Iterable[_Union[_UpdateConfigWarning_pb2.UpdateConfigWarning, _Mapping]]] = ..., resetAPIOrderSequence: _Optional[bool] = ...) -> None: ...
