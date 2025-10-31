from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='kp_query']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], .header-fresh-search-button")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href*='auth'], .login-button")
    LOGIN_FORM = (By.CSS_SELECTOR, ".auth-form, .login-form")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search-results, .film-list, .item")
    MOVIE_CARD = (By.CSS_SELECTOR, ".film, .movie, .item")
    
    @allure.step("Выполнить поиск фильма '{query}'")
    def search_movie(self, query):
        """Выполнить поиск фильма по запросу"""
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
    
    @allure.step("Перейти на страницу авторизации")
    def go_to_login(self):
        """Перейти на страницу авторизации"""
        self.click(self.LOGIN_BUTTON)
