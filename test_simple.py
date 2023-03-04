import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_size():
    browser.config.browser_name = 'firefox'
    browser.config.window_width = 720
    browser.config.window_height = 960


def test_google_positive(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
