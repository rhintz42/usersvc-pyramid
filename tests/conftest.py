import pytest
import os
from webtest import TestApp
from pyramid.paster import get_appsettings
from pyramid.paster import get_app
from pyramid import testing
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from usersvc import repos


def noop(*args, **kwargs):
    pass


def pytest_configure(config):
    os.environ['PYTEST'] = '1'


def pytest_unconfigure(config):
    del os.environ['PYTEST']


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true",
                     help="run slow tests")

here = os.path.dirname(__file__)
config_file = os.path.join(here, 'test.ini')
settings = get_appsettings(config_file)

# We don't want to hit cache during our tests
settings['cache.enabled'] = False


class MockDBSession(object):
    enabled = False
    session = None

    def check_if_enabled(self):
        if not self.enabled:
            raise Exception(
                "Database usage is disabled for unit tests")

    def execute(self, *args, **kwargs):
        self.check_if_enabled()

        return self.session.execute(*args, **kwargs)

    def close(self):
        pass

    @property
    def connection(self):
        self.check_if_enabled()
        return self.session.connection()


sess = MockDBSession()
# We want to monkey patch repos to not have a session, prevent
# non-integration tests from using it
repos.DBSession = sess

# The global non-ORM transaction
trans = None
usersvc_app = TestApp(get_app(config_file))


def should_use_trans(item):
    return 'integration' in item.keywords or 'functional' in item.keywords


@pytest.fixture()
def wsgiapp(request):
    """
    This will setup a test wsgi app for any test that accepts
    the argument wsgiapp
    """

    if should_use_trans(request):
        return usersvc_app


@pytest.fixture()
def session(request):
    """
    This will hande the db session to tests that declare session in
    their arguments
    """

    if should_use_trans(request):
        return sess


def pytest_runtest_setup(item):
    if 'slow' in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("need --runslow option to run")
        return

    # We never want tests to run in cache
    if should_use_trans(item):
        global trans
        global sess
        testing.setUp(settings=settings)
        engine = engine_from_config(settings, prefix='sqlalchemy.')
        connection = engine.connect()
        trans = connection.begin()
        DBSession = sessionmaker(bind=connection)

        # Override the existing database session with
        # one thats wrapped in a transaction
        sess.session = DBSession()
        sess.enabled = True


def pytest_runtest_teardown(item):
    if should_use_trans(item):
        global trans
        testing.tearDown()
        trans.rollback()
        sess.session.close()
        sess.enabled = False
