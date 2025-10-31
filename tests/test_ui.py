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
        """Проверка видимости строки поиска на главной странице"""
        with allure.step("Открыть главную страницу Кинопоиска"):
            self.main_page.open()
        
        with allure.step("Проверить видимость строки поиска"):
            assert self.main_page.is_visible(MainPage.SEARCH_INPUT), "Строка поиска не отображается на главной странице"
    
    @allure.story("Поиск фильмов") 
    @allure.title("КПС 12: Поиск по полному русскому названию фильма")
    def test_search_by_full_russian_title(self):
        """Поиск фильма по полному русскому названию"""
        with allure.step("Открыть главную страницу"):
            self.main_page.open()
        
        with allure.step(f"Выполнить поиск фильма '{settings.TEST_MOVIE_TITLE}'"):
            self.main_page.search_movie(settings.TEST_MOVIE_TITLE)
        
        with allure.step("Проверить наличие результатов поиска"):
            assert self.main_page.is_visible(MainPage.SEARCH_RESULTS), "Результаты поиска не отображаются"
    
    @allure.story("Поиск фильмов")
    @allure.title("КПС 13: Поиск по фрагменту названия")
    def test_search_by_title_fragment(self):
        """Поиск фильма по фрагменту названия"""
        with allure.step("Открыть главную страницу"):
            self.main_page.open()
        
        with allure.step(f"Выполнить поиск по фрагменту '{settings.TEST_MOVIE_FRAGMENT}'"):
            self.main_page.search_movie(settings.TEST_MOVIE_FRAGMENT)
        
        with allure.step("Проверить отображение результатов"):
            assert self.main_page.is_visible(MainPage.SEARCH_RESULTS), "Результаты поиска не отображаются"
    
    @allure.story("Поиск фильмов")
    @allure.title("КПС 14: Поиск по английскому названию")
    def test_search_by_english_title(self):
        """Поиск фильма по английскому названию"""
        with allure.step("Открыть главную страницу"):
            self.main_page.open()
        
        with allure.step("Выполнить поиск по английскому названию 'Interstellar'"):
            self.main_page.search_movie("Interstellar")
        
        with allure.step("Проверить наличие результатов"):
            assert self.main_page.is_visible(MainPage.SEARCH_RESULTS), "Результаты поиска не отображаются"
    
    @allure.story("Авторизация")
    @allure.title("КПС 1: Отображение формы авторизации")
    def test_login_form_display(self):
        """Проверка отображения формы авторизации"""
        with allure.step("Открыть главную страницу"):
            self.main_page.open()
        
        with allure.step("Перейти на страницу авторизации"):
            self.main_page.go_to_login()
        
        with allure.step("Проверить отображение формы авторизации"):
            assert self.main_page.is_visible(MainPage.LOGIN_FORM), "Форма авторизации не отображается"
