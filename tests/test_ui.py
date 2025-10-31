import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from config.settings import settings


@allure.feature("UI Тесты Кинопоиска")
@pytest.mark.ui
class TestKinopoiskUI:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.main_page = MainPage(self.driver)
        yield
        self.driver.quit()

    @allure.story("Поиск фильмов")
    @allure.title("КПС 11: Строка поиска видна на главной странице")
    def test_search_input_visible(self):
        self.main_page.open()
        assert self.main_page.is_visible(MainPage.SEARCH_INPUT)

    @allure.story("Поиск фильмов")
    @allure.title("КПС 12: Поиск по полному русскому названию фильма")
    def test_search_by_full_russian_title(self):
        self.main_page.open()
        self.main_page.search_movie(settings.TEST_MOVIE_TITLE)
        assert self.main_page.is_visible(MainPage.SEARCH_RESULTS)

    @allure.story("Поиск фильмов")
    @allure.title("КПС 13: Поиск по фрагменту названия")
    def test_search_by_title_fragment(self):
        self.main_page.open()
        self.main_page.search_movie(settings.TEST_MOVIE_FRAGMENT)
        assert self.main_page.is_visible(MainPage.SEARCH_RESULTS)

    @allure.story("Поиск фильмов")
    @allure.title("КПС 14: Поиск по английскому названию")
    def test_search_by_english_title(self):
        self.main_page.open()
        self.main_page.search_movie("Interstellar")
        assert self.main_page.is_visible(MainPage.SEARCH_RESULTS)

    @allure.story("Авторизация")
    @allure.title("КПС 1: Отображение формы авторизации")
    def test_login_form_display(self):
        self.main_page.open()
        self.main_page.go_to_login()
        assert self.main_page.is_visible(MainPage.LOGIN_FORM)
