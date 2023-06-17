"""
Login to pathfinder.

>>> from pathfinder.operators.login import Login
>>> c = {"host": "pathfinder", "user": "Admin", "pass": "Admin"}
>>> l = Login(client=client, config=c)
>>> l.execute()
True
>>> c = {"host": "pathfinder", "user": "Admin", "pass": "Nope"}
>>> l = Login(client=client, config=c)
>>> l.execute()
False
"""

from pathfinder.operators.base import BaseOperator


class LoginException(Exception):
    pass


class Login(BaseOperator):
    config = {"user": "Admin", "pass": "Admin"}

    def execute(self) -> bool:
        self.client.write(
            "LOGIN {} {}".format(
                self.config.get("user"), self.config.get("pass")
            ).encode("ascii")
            + b"\r\n"
        )
        index, *_ = self.client.expect(
            [b"login failed", b"login successful"], timeout=1
        )
        return index == 1
