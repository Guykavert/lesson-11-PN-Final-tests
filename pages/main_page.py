from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='kp_query']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href*='auth']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".auth-form")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search-results")

    @allure.step("Выполнить поиск фильма '{query}'")
    def search_movie(self, query):
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    @allure.step("Перейти на страницу авторизации")
    def go_to_login(self):
        self.click(self.LOGIN_BUTTON)
