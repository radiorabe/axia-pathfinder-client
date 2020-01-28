import pytest

from pathfinder.parser import ResponseParser

_PARSER_TESTDATA = [
    ("indi Devices#0", {"path": "Devices#0", "info": {}}),
    ("indi MemorySlots#0", {"path": "MemorySlots#0", "info": {}}),
    (
        'indi MemorySlots#0.MemorySlot#Test SlotName=Test, SlotValue=MyValue, SubVersion="0001-01-01T00:00:00.000+00:00"',
        {
            "path": "MemorySlots#0.MemorySlot#Test",
            "info": {
                "SlotName": "Test",
                "SlotValue": "MyValue",
                "SubVersion": '"0001-01-01T00:00:00.000+00:00"',
            },
        },
    ),
    ("GPO 1 lllhh", {"number": "1", "pins": [True, True, True, False, False]}),
]


class TestParser:
    @pytest.mark.parametrize("string,obj", _PARSER_TESTDATA)
    def test_parse(self, string, obj):
        assert ResponseParser().parse(string) == obj
