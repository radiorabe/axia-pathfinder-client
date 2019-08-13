from abc import ABC, abstractmethod


class BaseOperator(ABC):
    config = {}

    def __init__(self, client, config={}):
        self.client = client.client
        self.config = {**self.config, **config}

    @abstractmethod
    def execute(self):  # pragma: no cover
        pass
