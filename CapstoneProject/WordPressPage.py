from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class WordPressPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)

    def open_homepage(self):
        self.browser.get("https://wordpress.org/")
        assert "WordPress.org" in self.browser.title
        print(f"✓ Homepage title verified: {self.browser.title}")

    def navigate_to_themes(self):
        extend_menu = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Extend']"))
        )
        ActionChains(self.browser).move_to_element(extend_menu).perform()

        themes_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Themes"))
        )
        themes_link.click()
        print("✓ Navigated to Themes page")

    def search_theme(self, theme_name):
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "wp-block-search__input-8"))
        )
        search_input.clear()
        search_input.send_keys(theme_name)
        search_input.send_keys(Keys.ENTER)
        print(f"✓ Searched for theme: {theme_name}")

    def open_theme_page(self, theme_name):
        theme_card_xpath = f"//h2[contains(text(), '{theme_name}')]"
        theme_card = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, theme_card_xpath))
        )
        self.browser.execute_script("arguments[0].scrollIntoView({block:'center'});", theme_card)
        theme_card.click()
        print(f"✓ Opened theme page for: {theme_name}")

    def verify_theme_title(self, theme_name):
        theme_title_h1 = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )
        assert theme_name in theme_title_h1.text
        print(f"✓ Theme page title verified: {theme_title_h1.text}")

