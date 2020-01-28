import pytest

from pathfinder.operators.get import Get

_GET_TESTDATA = [
    ([b"indi Devices#0\r\n"], [{"path": "Devices#0", "info": {}}]),
    (
        [b"indi Devices#0\r\n", b"indi MemorySlots#0\r\n"],
        [{"path": "Devices#0", "info": {}}, {"path": "MemorySlots#0", "info": {}}],
    ),
    (
        [b"indi MemorySlots#0.MemorySlot#Test SlotName=Test, SlotValue=MyValue\r\n"],
        [
            {
                "path": "MemorySlots#0.MemorySlot#Test",
                "info": {"SlotName": "Test", "SlotValue": "MyValue"},
            }
        ],
    ),
]


class TestGetOperator:
    @pytest.mark.parametrize("values,expected", _GET_TESTDATA)
    def test_get_root(self, client, values, expected):
        get = Get(client=client, config={"path": "."})

        results = [b"\r\n"] + values + [b""]

        def next_result(string, timeout=1):
            return results.pop(0)

        get.client.read_until.side_effect = next_result

        results = get.execute()

        for i, value in enumerate(expected):
            assert results[i] == value

        get.client.write.assert_called_with(b"GET .\r\n")
        get.client.read_until.assert_called_with(b"\r\n", timeout=1)
