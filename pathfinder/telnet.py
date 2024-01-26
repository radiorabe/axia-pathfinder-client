"""
Wrapper around telnetlib.

>>> from pathfinder.telnet import TelnetClient
>>> tc = TelnetClient()
>>> tc.connect()
>>> tc.disconnect()
"""

import logging
import telnetlib

logger = logging.getLogger(__name__)


class TelnetClientException(Exception):
    """Exceptions raised by TelnetClient."""

    pass


class TelnetClient:
    """Telnet client handler."""

    config = {"host": "localhost", "port": 9600, "timeout": 1}

    def __init__(self, config={}):
        self.config = {**self.config, **config}
        self.client = telnetlib.Telnet()

    def connect(self):
        """Connect the client."""
        try:
            self.client.open(
                self.config.get("host"),
                self.config.get("port"),
                self.config.get("timeout"),
            )
        except Exception as ex:
            logger.error("Error connecting telnet client")
            raise TelnetClientException(ex)

    def disconnect(self):
        """Disconnect the client."""
        try:
            self.client.close()
        except Exception as ex:
            logger.error("Error disconnecting telnet client")
            raise TelnetClientException(ex)
