from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApiSettingsConfig(_message.Message):
    __slots__ = ("readOnlyApi", "totalQuantityForMutualFunds", "downloadOpenOrdersOnConnection", "includeVirtualFxPositions", "prepareDailyPnL", "sendStatusUpdatesForVolatilityOrders", "encodeApiMessages", "socketPort", "useNegativeAutoRange", "createApiMessageLogFile", "includeMarketDataInLogFile", "exposeTradingScheduleToApi", "splitInsuredDepositFromCashBalance", "sendZeroPositionsForTodayOnly", "letApiAccountRequestsSwitchSubscription", "useAccountGroupsWithAllocationMethods", "loggingLevel", "masterClientId", "bulkDataTimeout", "componentExchSeparator", "showForexDataIn1_10Pips", "allowForexTradingIn1_10Pips", "roundAccountValuesToNearestWholeNumber", "sendMarketDataInLotsForUsStocks", "showAdvancedOrderRejectInUi", "rejectMessagesAboveMaxRate", "maintainConnectionOnIncorrectFields", "compatibilityModeNasdaqStocks", "sendInstrumentTimezone", "sendForexDataInCompatibilityMode", "maintainAndResubmitOrdersOnReconnect", "historicalDataMaxSize", "autoReportNettingEventContractTrades", "optionExerciseRequestType", "allowLocalhostOnly", "trustedIPs")
    READONLYAPI_FIELD_NUMBER: _ClassVar[int]
    TOTALQUANTITYFORMUTUALFUNDS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADOPENORDERSONCONNECTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDEVIRTUALFXPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    PREPAREDAILYPNL_FIELD_NUMBER: _ClassVar[int]
    SENDSTATUSUPDATESFORVOLATILITYORDERS_FIELD_NUMBER: _ClassVar[int]
    ENCODEAPIMESSAGES_FIELD_NUMBER: _ClassVar[int]
    SOCKETPORT_FIELD_NUMBER: _ClassVar[int]
    USENEGATIVEAUTORANGE_FIELD_NUMBER: _ClassVar[int]
    CREATEAPIMESSAGELOGFILE_FIELD_NUMBER: _ClassVar[int]
    INCLUDEMARKETDATAINLOGFILE_FIELD_NUMBER: _ClassVar[int]
    EXPOSETRADINGSCHEDULETOAPI_FIELD_NUMBER: _ClassVar[int]
    SPLITINSUREDDEPOSITFROMCASHBALANCE_FIELD_NUMBER: _ClassVar[int]
    SENDZEROPOSITIONSFORTODAYONLY_FIELD_NUMBER: _ClassVar[int]
    LETAPIACCOUNTREQUESTSSWITCHSUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USEACCOUNTGROUPSWITHALLOCATIONMETHODS_FIELD_NUMBER: _ClassVar[int]
    LOGGINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    MASTERCLIENTID_FIELD_NUMBER: _ClassVar[int]
    BULKDATATIMEOUT_FIELD_NUMBER: _ClassVar[int]
    COMPONENTEXCHSEPARATOR_FIELD_NUMBER: _ClassVar[int]
    SHOWFOREXDATAIN1_10PIPS_FIELD_NUMBER: _ClassVar[int]
    ALLOWFOREXTRADINGIN1_10PIPS_FIELD_NUMBER: _ClassVar[int]
    ROUNDACCOUNTVALUESTONEARESTWHOLENUMBER_FIELD_NUMBER: _ClassVar[int]
    SENDMARKETDATAINLOTSFORUSSTOCKS_FIELD_NUMBER: _ClassVar[int]
    SHOWADVANCEDORDERREJECTINUI_FIELD_NUMBER: _ClassVar[int]
    REJECTMESSAGESABOVEMAXRATE_FIELD_NUMBER: _ClassVar[int]
    MAINTAINCONNECTIONONINCORRECTFIELDS_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITYMODENASDAQSTOCKS_FIELD_NUMBER: _ClassVar[int]
    SENDINSTRUMENTTIMEZONE_FIELD_NUMBER: _ClassVar[int]
    SENDFOREXDATAINCOMPATIBILITYMODE_FIELD_NUMBER: _ClassVar[int]
    MAINTAINANDRESUBMITORDERSONRECONNECT_FIELD_NUMBER: _ClassVar[int]
    HISTORICALDATAMAXSIZE_FIELD_NUMBER: _ClassVar[int]
    AUTOREPORTNETTINGEVENTCONTRACTTRADES_FIELD_NUMBER: _ClassVar[int]
    OPTIONEXERCISEREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOWLOCALHOSTONLY_FIELD_NUMBER: _ClassVar[int]
    TRUSTEDIPS_FIELD_NUMBER: _ClassVar[int]
    readOnlyApi: bool
    totalQuantityForMutualFunds: bool
    downloadOpenOrdersOnConnection: bool
    includeVirtualFxPositions: bool
    prepareDailyPnL: bool
    sendStatusUpdatesForVolatilityOrders: bool
    encodeApiMessages: str
    socketPort: int
    useNegativeAutoRange: bool
    createApiMessageLogFile: bool
    includeMarketDataInLogFile: bool
    exposeTradingScheduleToApi: bool
    splitInsuredDepositFromCashBalance: bool
    sendZeroPositionsForTodayOnly: bool
    letApiAccountRequestsSwitchSubscription: bool
    useAccountGroupsWithAllocationMethods: bool
    loggingLevel: str
    masterClientId: int
    bulkDataTimeout: int
    componentExchSeparator: str
    showForexDataIn1_10Pips: bool
    allowForexTradingIn1_10Pips: bool
    roundAccountValuesToNearestWholeNumber: bool
    sendMarketDataInLotsForUsStocks: bool
    showAdvancedOrderRejectInUi: bool
    rejectMessagesAboveMaxRate: bool
    maintainConnectionOnIncorrectFields: bool
    compatibilityModeNasdaqStocks: bool
    sendInstrumentTimezone: str
    sendForexDataInCompatibilityMode: bool
    maintainAndResubmitOrdersOnReconnect: bool
    historicalDataMaxSize: int
    autoReportNettingEventContractTrades: bool
    optionExerciseRequestType: str
    allowLocalhostOnly: bool
    trustedIPs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, readOnlyApi: _Optional[bool] = ..., totalQuantityForMutualFunds: _Optional[bool] = ..., downloadOpenOrdersOnConnection: _Optional[bool] = ..., includeVirtualFxPositions: _Optional[bool] = ..., prepareDailyPnL: _Optional[bool] = ..., sendStatusUpdatesForVolatilityOrders: _Optional[bool] = ..., encodeApiMessages: _Optional[str] = ..., socketPort: _Optional[int] = ..., useNegativeAutoRange: _Optional[bool] = ..., createApiMessageLogFile: _Optional[bool] = ..., includeMarketDataInLogFile: _Optional[bool] = ..., exposeTradingScheduleToApi: _Optional[bool] = ..., splitInsuredDepositFromCashBalance: _Optional[bool] = ..., sendZeroPositionsForTodayOnly: _Optional[bool] = ..., letApiAccountRequestsSwitchSubscription: _Optional[bool] = ..., useAccountGroupsWithAllocationMethods: _Optional[bool] = ..., loggingLevel: _Optional[str] = ..., masterClientId: _Optional[int] = ..., bulkDataTimeout: _Optional[int] = ..., componentExchSeparator: _Optional[str] = ..., showForexDataIn1_10Pips: _Optional[bool] = ..., allowForexTradingIn1_10Pips: _Optional[bool] = ..., roundAccountValuesToNearestWholeNumber: _Optional[bool] = ..., sendMarketDataInLotsForUsStocks: _Optional[bool] = ..., showAdvancedOrderRejectInUi: _Optional[bool] = ..., rejectMessagesAboveMaxRate: _Optional[bool] = ..., maintainConnectionOnIncorrectFields: _Optional[bool] = ..., compatibilityModeNasdaqStocks: _Optional[bool] = ..., sendInstrumentTimezone: _Optional[str] = ..., sendForexDataInCompatibilityMode: _Optional[bool] = ..., maintainAndResubmitOrdersOnReconnect: _Optional[bool] = ..., historicalDataMaxSize: _Optional[int] = ..., autoReportNettingEventContractTrades: _Optional[bool] = ..., optionExerciseRequestType: _Optional[str] = ..., allowLocalhostOnly: _Optional[bool] = ..., trustedIPs: _Optional[_Iterable[str]] = ...) -> None: ...
