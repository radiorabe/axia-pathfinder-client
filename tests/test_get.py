import pytest

from pathfinder.operators.get import Get

_GET_TESTDATA = [
    (
        [b"indi Devices#0\r\n"],
        [{"obj": "Object((ObjectPart(Devices#0)))", "params": {}}],
    ),
    (
        [b"indi Devices#0\r\n", b"indi MemorySlots#0"],
        [
            {"obj": "Object((ObjectPart(Devices#0)))", "params": {}},
            {"obj": "Object((ObjectPart(MemorySlots#0)))", "params": {}},
        ],
    ),
    (
        [b"indi MemorySlots#0.MemorySlot#Test SlotName=Test, SlotValue=MyValue\r\n"],
        [
            {
                "obj": "Object((ObjectPart(MemorySlots#0), ObjectPart(MemorySlot#Test)))",
                "params": {"SlotName": "Test", "SlotValue": "MyValue"},
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
            assert results[i][0] == "INDI"
            assert str(results[i][1]) == value.get("obj")
            assert results[i][2] == value.get("params")

        get.client.write.assert_called_with(b"GET .\r\n")
        get.client.read_until.assert_called_with(b"\r\n", timeout=1)
