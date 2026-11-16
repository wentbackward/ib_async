from . import OrdersSmartRoutingConfig_pb2 as _OrdersSmartRoutingConfig_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrdersConfig(_message.Message):
    __slots__ = ("smartRouting",)
    SMARTROUTING_FIELD_NUMBER: _ClassVar[int]
    smartRouting: _OrdersSmartRoutingConfig_pb2.OrdersSmartRoutingConfig
    def __init__(self, smartRouting: _Optional[_Union[_OrdersSmartRoutingConfig_pb2.OrdersSmartRoutingConfig, _Mapping]] = ...) -> None: ...
