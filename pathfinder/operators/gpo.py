"""Get data from pathfinder."""

from pathfinder.operators.base import BaseOperator
from pathfinder.parser import ResponseParser


class GPOException(Exception):
    pass


class GPO(BaseOperator):
    config = {"number": "1"}

    def execute(self):
        p = ResponseParser()
        self.client.write(
            "GPO {}".format(self.config.get("number")).encode("ascii") + b"\r\n"
        )
        results = []
        while True:
            data = self.client.read_until(b"\r\n", timeout=1)
            if data == b"":
                break
            if data != b"\r\n":
                results.append(p.parse(data.decode("ascii").rstrip("\r\n")))
        return results
