from abc import ABC, abstractmethod

from ..telnet import TelnetClient


class BaseOperator(ABC):
    config = {}

    def __init__(self, client: TelnetClient, config={}):
        self.client = client.client
        self.config = {**self.config, **config}

    @abstractmethod
    def execute(self):  # pragma: no cover
        pass
