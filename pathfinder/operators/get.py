"""Get data from pathfinder."""

from pathfinder.operators.base import BaseOperator
from pathfinder.parser import ResponseParser


class GetException(Exception):
    pass


class Get(BaseOperator):
    config = {"path": "."}

    def execute(self):
        p = ResponseParser()
        self.client.write(
            "GET {}".format(self.config.get("path")).encode("ascii") + b"\r\n"
        )
        results = []
        while True:
            data = self.client.read_until(b"\r\n", timeout=1)
            if data == b"":
                break
            if data != b"\r\n":
                results.append(p.parse(data.decode("ascii").rstrip("\r\n")))
        return results
