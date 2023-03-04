import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_size():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 400
    browser.config.window_height = 600


def test_google_positive(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_not_found(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('рвоароариаримфварваапу').press_enter()
    browser.element('.card-section').should(have.text('По запросу рвоароариаримфварваапу ничего не найдено. '))
