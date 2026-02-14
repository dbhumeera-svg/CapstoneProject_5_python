import pytest
from selenium import webdriver
from WordPressPage import WordPressPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_and_open_theme(browser):
    wp = WordPressPage(browser)
    wp.open_homepage()
    wp.navigate_to_themes()
    wp.search_theme("Hello Biz")
    wp.open_theme_page("Hello Biz")
    wp.verify_theme_title("Hello Biz")
