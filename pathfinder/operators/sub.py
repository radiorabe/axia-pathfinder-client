"""
SUB operator

https://docs.telosalliance.com/pathfinder-core-pro/pathfindercore-pro/appendix-a-sapv2#subscription-examples
"""

from typing import NoReturn

from pathfinder.operators.base import BaseOperator


class Sub(BaseOperator):
    config = {"path": "."}

    def execute(self) -> NoReturn:
        self.client.write(f"SUB {self.config.get('path')}".encode("ascii") + b"\r\n")
