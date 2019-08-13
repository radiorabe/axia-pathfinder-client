import pytest

from pathfinder.parser import ResponseParser

_PARSER_TESTDATA = [
    ("indi Devices#0", "INDI", "Object((ObjectPart(Devices#0)))", {}),
    ("indi MemorySlots#0", "INDI", "Object((ObjectPart(MemorySlots#0)))", {}),
    (
        'indi MemorySlots#0.MemorySlot#Test SlotName=Test, SlotValue=MyValue, SubVersion="0001-01-01T00:00:00.000+00:00"',
        "INDI",
        "Object((ObjectPart(MemorySlots#0), ObjectPart(MemorySlot#Test)))",
        {
            "SlotName": "Test",
            "SlotValue": "MyValue",
            "SubVersion": '"0001-01-01T00:00:00.000+00:00"',
        },
    ),
]


class TestParser:
    @pytest.mark.parametrize("string,type,strobj,params", _PARSER_TESTDATA)
    def test_parse(self, string, type, strobj, params):
        parser = ResponseParser()
        results = parser.parse(string)
        assert results[0] == type
        assert str(results[1]) == strobj
        assert results[2] == params
