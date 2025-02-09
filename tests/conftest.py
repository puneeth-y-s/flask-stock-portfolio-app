import os
import pytest
from project import create_app
from flask import current_app, request

# @pytest.fixture(scope='module')
# def test_client():
#     # Set the Testing configuration prior to creating the Flask application
#     os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
#     flask_app = create_app()

#     # Create a test client using the Flask application configured for testing
#     testing_client = flask_app.test_client()

#     return testing_client

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app()
#     flask_app.config.from_object('config.TestingConfig')

#     # Create a test client using the Flask application configured for testing
#     testing_client = flask_app.test_client()

#     # Establish an application context
#     ctx = flask_app.app_context()
#     ctx.push()

#     current_app.logger.info('In the test_client() fixture...')

#     # Pop the application context from the stack
#     ctx.pop()

#     yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context before accessing the logger
        with flask_app.app_context():
            current_app.logger.info('In the test_client() fixture...')

        yield testing_client  # this is where the testing happens!

