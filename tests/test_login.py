from pathfinder.operators.login import Login


class TestLoginOperator:
    def test_login_init_empty_params(self, client):
        login = Login(client=client)
        assert login.config.get("user") == "Admin"
        assert login.config.get("pass") == "Admin"

    def test_login_init_with_telnetclient_conf(self, client):
        loginconf = {"user": "user", "pass": "pass"}
        login = Login(client=client, config=loginconf)
        assert login.config.get("user") == "user"
        assert login.config.get("pass") == "pass"

    def test_login_passes_args(self, client):
        login = Login(client=client, config={"user": "user", "pass": "pass"})

        def login_results(msg, timeout=0):
            return [0, "", 0]

        login.client.expect.side_effect = login_results

        login.execute()

        login.client.write.assert_called_with(b"LOGIN user pass\r\n")

    def test_login_execute_ok(self, client):
        login = Login(client=client)

        def login_results(msg, timeout=0):
            return [1, "login successful", 16]

        login.client.expect.side_effect = login_results

        assert login.execute() is True

        login.client.write.assert_called_with(b"LOGIN Admin Admin\r\n")

        login.client.expect.assert_called_with(
            [b"login failed", b"login successful"], timeout=1
        )

    def test_login_execute_nok(self, client):
        login = Login(client=client, config={"pass": "NOK"})

        def login_results(msg, timeout=0):
            return [0, "login failed", 12]

        login.client.expect.side_effect = login_results

        assert login.execute() is False

        login.client.write.assert_called_with(b"LOGIN Admin NOK\r\n")

        login.client.expect.assert_called_with(
            [b"login failed", b"login successful"], timeout=1
        )
