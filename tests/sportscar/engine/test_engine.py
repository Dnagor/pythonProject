from pytest import mark


@mark.smoke
@mark.engine
def test_engine_functions(chrome_browser):
    chrome_browser.get("prod.practitest.com")
    assert True
