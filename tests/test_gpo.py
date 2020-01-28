import pytest

from pathfinder.operators.gpo import GPO

_GPO_TESTDATA = [
    ([b"GPO 0 hlhlh\r\n"], [{"number": "0", "pins": [False, True, False, True, False]}])
]


class TestGetOperator:
    @pytest.mark.parametrize("values,expected", _GPO_TESTDATA)
    def test_get_root(self, client, values, expected):
        get = GPO(client=client, config={"number": "0"})

        results = [b"\r\n"] + values + [b""]

        def next_result(string, timeout=1):
            return results.pop(0)

        get.client.read_until.side_effect = next_result

        results = get.execute()

        for i, value in enumerate(expected):
            assert results[i] == value

        get.client.write.assert_called_with(b"GPO 0\r\n")
        get.client.read_until.assert_called_with(b"\r\n", timeout=1)
