from . import ApiPrecautionsConfig_pb2 as _ApiPrecautionsConfig_pb2
from . import ApiSettingsConfig_pb2 as _ApiSettingsConfig_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApiConfig(_message.Message):
    __slots__ = ("precautions", "settings")
    PRECAUTIONS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    precautions: _ApiPrecautionsConfig_pb2.ApiPrecautionsConfig
    settings: _ApiSettingsConfig_pb2.ApiSettingsConfig
    def __init__(self, precautions: _Optional[_Union[_ApiPrecautionsConfig_pb2.ApiPrecautionsConfig, _Mapping]] = ..., settings: _Optional[_Union[_ApiSettingsConfig_pb2.ApiSettingsConfig, _Mapping]] = ...) -> None: ...
