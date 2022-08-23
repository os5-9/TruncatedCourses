from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_make_parametrize_id(config, val): return repr(val)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or edge")
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en ... etc.")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        print("\nstart Edge browser for test..")
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")
    yield driver
    print("\nquit browser..")
    driver.quit()
