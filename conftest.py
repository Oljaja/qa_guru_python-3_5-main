import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True
    browser.config.window_width = 1019
    browser.config.window_height = 598

