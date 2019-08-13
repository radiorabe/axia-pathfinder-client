from pathfinder.operators.base import BaseOperator


class MyOperator(BaseOperator):
    def execute(self):
        pass


class TestBaseOperator:
    def test_base_init(self, client):
        base = MyOperator(client=client)
        assert base.client == client.client
