import telnetlib
from unittest.mock import patch

from pytest import raises

from pathfinder.telnet import TelnetClient, TelnetClientException


class TestTelnetClient:
    def test_telnetclient_init_empty_params(self):
        telnetclient = TelnetClient()
        assert telnetclient.config.get("host") == "localhost"
        assert telnetclient.config.get("port") == 9600

    def test_telnetclient_init_with_telnetclient_conf(self):
        telnetclientconf = {"host": "host", "port": 20000}
        telnetclient = TelnetClient(telnetclientconf)
        assert telnetclient.config.get("host") == "host"
        assert telnetclient.config.get("port") == 20000

    @patch.object(telnetlib, "Telnet")
    def test_telnetclient_connect(self, mocked):
        telnetclientconf = {"host": "host", "port": 20000}
        telnetclient = TelnetClient(telnetclientconf)

        telnetclient.connect()
        mocked.assert_called_with()
        telnetclient.client.open.assert_called_with(
            telnetclientconf["host"], telnetclientconf["port"], 1
        )

    @patch.object(telnetlib.Telnet, "open")
    def test_telnetclient_connect_exception(self, mocked):
        mocked.side_effect = Exception("In your face")

        telnetclientconf = {"host": "host", "port": 20000}
        telnetclient = TelnetClient(telnetclientconf)

        with raises(TelnetClientException):
            telnetclient.connect()

    @patch.object(telnetlib.Telnet, "close")
    def test_telnetclient_disconnect_exception(self, mocked):
        mocked.side_effect = Exception("In your face !")

        telnetclientconf = {"host": "host", "port": 20000}
        telnetclient = TelnetClient(telnetclientconf)

        with raises(TelnetClientException):
            telnetclient.disconnect()

    @patch.object(telnetlib, "Telnet")
    def test_telnetclient_disconnect(self, mocked):
        telnetclientconf = {"host": "host", "port": 20000}
        telnetclient = TelnetClient(telnetclientconf)

        telnetclient.connect()
        telnetclient.disconnect()
        telnetclient.client.close.assert_called_with()
