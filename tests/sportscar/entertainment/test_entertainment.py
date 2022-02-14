from pytest import mark


@mark.not_smoke
@mark.entertainment
def test_entertainment_functions(chrome_browser):
    chrome_browser.get("www.softserve.udemy.com")
    assert True
