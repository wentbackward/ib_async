from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrdersSmartRoutingConfig(_message.Message):
    __slots__ = ("seekPriceImprovement", "preOpenReroute", "doNotRouteToDarkPools", "defaultAlgorithm")
    SEEKPRICEIMPROVEMENT_FIELD_NUMBER: _ClassVar[int]
    PREOPENREROUTE_FIELD_NUMBER: _ClassVar[int]
    DONOTROUTETODARKPOOLS_FIELD_NUMBER: _ClassVar[int]
    DEFAULTALGORITHM_FIELD_NUMBER: _ClassVar[int]
    seekPriceImprovement: bool
    preOpenReroute: bool
    doNotRouteToDarkPools: bool
    defaultAlgorithm: str
    def __init__(self, seekPriceImprovement: _Optional[bool] = ..., preOpenReroute: _Optional[bool] = ..., doNotRouteToDarkPools: _Optional[bool] = ..., defaultAlgorithm: _Optional[str] = ...) -> None: ...
