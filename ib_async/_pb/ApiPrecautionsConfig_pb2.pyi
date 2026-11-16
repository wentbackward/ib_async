from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApiPrecautionsConfig(_message.Message):
    __slots__ = ("bypassOrderPrecautions", "bypassBondWarning", "bypassNegativeYieldConfirmation", "bypassCalledBondWarning", "bypassSameActionPairTradeWarning", "bypassFlaggedAccountsWarning", "bypassPriceBasedVolatilityWarning", "bypassRedirectOrderWarning", "bypassNoOverfillProtection", "bypassRouteMarketableToBBO")
    BYPASSORDERPRECAUTIONS_FIELD_NUMBER: _ClassVar[int]
    BYPASSBONDWARNING_FIELD_NUMBER: _ClassVar[int]
    BYPASSNEGATIVEYIELDCONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    BYPASSCALLEDBONDWARNING_FIELD_NUMBER: _ClassVar[int]
    BYPASSSAMEACTIONPAIRTRADEWARNING_FIELD_NUMBER: _ClassVar[int]
    BYPASSFLAGGEDACCOUNTSWARNING_FIELD_NUMBER: _ClassVar[int]
    BYPASSPRICEBASEDVOLATILITYWARNING_FIELD_NUMBER: _ClassVar[int]
    BYPASSREDIRECTORDERWARNING_FIELD_NUMBER: _ClassVar[int]
    BYPASSNOOVERFILLPROTECTION_FIELD_NUMBER: _ClassVar[int]
    BYPASSROUTEMARKETABLETOBBO_FIELD_NUMBER: _ClassVar[int]
    bypassOrderPrecautions: bool
    bypassBondWarning: bool
    bypassNegativeYieldConfirmation: bool
    bypassCalledBondWarning: bool
    bypassSameActionPairTradeWarning: bool
    bypassFlaggedAccountsWarning: bool
    bypassPriceBasedVolatilityWarning: bool
    bypassRedirectOrderWarning: bool
    bypassNoOverfillProtection: bool
    bypassRouteMarketableToBBO: bool
    def __init__(self, bypassOrderPrecautions: _Optional[bool] = ..., bypassBondWarning: _Optional[bool] = ..., bypassNegativeYieldConfirmation: _Optional[bool] = ..., bypassCalledBondWarning: _Optional[bool] = ..., bypassSameActionPairTradeWarning: _Optional[bool] = ..., bypassFlaggedAccountsWarning: _Optional[bool] = ..., bypassPriceBasedVolatilityWarning: _Optional[bool] = ..., bypassRedirectOrderWarning: _Optional[bool] = ..., bypassNoOverfillProtection: _Optional[bool] = ..., bypassRouteMarketableToBBO: _Optional[bool] = ...) -> None: ...
