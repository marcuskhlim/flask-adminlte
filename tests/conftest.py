import pytest
from apps.config import config_dict
from apps import create_app
import os

@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    DEBUG = (os.getenv('DEBUG', 'False') == 'True')

    # The configuration
    get_config_mode = 'Debug' if DEBUG else 'Production'

    try:

        # Load the configuration using the default values
        app_config = config_dict[get_config_mode.capitalize()]

    except KeyError:
        exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

    _app = create_app(config=app_config)

    #_app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
