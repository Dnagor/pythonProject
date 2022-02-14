import pytest


@pytest.mark.environment
def test_environment_is_qa(app_config):
    assert app_config.base_url == "https://myqa-env.com"
    assert app_config.app_port == 80


@pytest.mark.environment
def test_environment_is_dev(app_config):
    assert app_config.base_url == "https://mydev-env.com"
    assert app_config.app_port == 8080
