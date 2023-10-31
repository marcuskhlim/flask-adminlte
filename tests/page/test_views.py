from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('home_blueprint.index'))
        assert response.status_code == 200

    def test_login_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('authentication_blueprint.login'))
        assert response.status_code == 200

    def test_register_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('authentication_blueprint.register'))
        assert response.status_code == 200
