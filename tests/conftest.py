import pytest
from selenium import webdriver

from tests.config import Config


@pytest.fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
