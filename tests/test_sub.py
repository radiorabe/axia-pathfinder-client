from pathfinder.operators.sub import Sub


class TestGetOperator:
    def test_sub_root(self, client):
        sub = Sub(client=client, config={"path": "."})

        sub.execute()

        sub.client.write.assert_called_with(b"SUB .\r\n")
