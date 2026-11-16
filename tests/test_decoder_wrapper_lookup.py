"""The binary decoder finds the wrapper method when each message arrives.

``Decoder.wrap`` used to bind the wrapper method once, when the client
was built, so a method replaced on the wrapper instance afterwards was
never called on the binary path. The protobuf handlers already looked
the method up on each call; both paths now behave the same way.
"""

from __future__ import annotations

from types import SimpleNamespace

from ib_async import IB
from ib_async.decoder import Decoder
from ib_async.runtime import Tally

# updateMktDepthL2: msgId 13, version, reqId 9, position 0, market maker
# "MM", operation 0, side 1, price 4999.75, size 3, isSmartDepth 0.
_DEPTH_L2 = ["13", "1", "9", "0", "MM", "0", "1", "4999.75", "3", "0"]


def test_a_method_replaced_after_the_client_is_built_is_called():
    ib = IB()
    seen = []
    ib.wrapper.updateMktDepthL2 = lambda *args: seen.append(args)

    ib.client.decoder.interpret(_DEPTH_L2)

    assert seen == [(9, 0, "MM", 0, 1, 4999.75, 3.0, False)]


def test_a_method_added_after_the_decoder_is_built_is_called():
    wrapper = SimpleNamespace()
    decoder = Decoder(wrapper, serverVersion=176)
    seen = []
    wrapper.updateMktDepthL2 = lambda *args: seen.append(args)

    decoder.interpret(_DEPTH_L2)

    assert len(seen) == 1


def test_a_wrapper_without_the_method_skips_the_message():
    tally = Tally()
    decoder = Decoder(SimpleNamespace(), serverVersion=176, tally=tally)

    decoder.interpret(_DEPTH_L2)

    assert tally.decodeFailures == 0
    assert tally.unknownMessages == 0
