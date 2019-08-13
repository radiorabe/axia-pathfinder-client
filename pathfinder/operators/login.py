"""
Login to pathfinder.

>>> from pathfinder.operators.login import Login
>>> l = Login(client=client, config={"host": "pathfinder", "user": "Admin", "pass": "Admin"})
>>> l.execute()
True
>>> l = Login(client=client, config={"host": "pathfinder", "user": "Admin", "pass": "Nope"})
>>> l.execute()
False
"""

from pathfinder.operators.base import BaseOperator


class LoginException(Exception):
    pass


class Login(BaseOperator):
    config = {"user": "Admin", "pass": "Admin"}

    def execute(self):
        self.client.write(
            "LOGIN {0} {1}".format(
                self.config.get("user"), self.config.get("pass")
            ).encode("ascii")
            + b"\r\n"
        )
        index, *_ = self.client.expect(
            [b"login failed", b"login successful"], timeout=1
        )
        return index == 1
