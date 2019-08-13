import telnetlib
from unittest.mock import patch

import pytest

from pathfinder.telnet import TelnetClient


@pytest.fixture()
@patch.object(telnetlib, "Telnet")
def client(telnet):
    tc = TelnetClient()
    telnet.assert_called_with()
    return tc
