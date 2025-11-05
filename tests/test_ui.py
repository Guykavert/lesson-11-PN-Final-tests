import pytest
import allure
import os
from pages.main_page import MainPage
from config.constants import constants


@allure.feature("UI Тесты Кинопоиска")
@pytest.mark.ui
class TestKinopoiskUI:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        ci_env = os.getenv('CI')
        if ci_env:
            pytest.skip("UI tests skipped")
        self.main_page = MainPage(browser)

    @allure.story("Авторизация")
    @allure.title("КПС 1: Отображение формы авторизации")
    def test_login_form_display(self):
        self.main_page.open()
        self.main_page.go_to_login()
        visible = self.main_page.is_visible(MainPage.LOGIN_FORM)
        assert visible, "Login form not visible"

    @pytest.mark.parametrize("search_query,expected_text", [
        (constants.TEST_MOVIE_TITLE, "Интерстеллар"),
        (constants.TEST_MOVIE_FRAGMENT, "Брат"),
        ("Interstellar", "Interstellar")
    ])
    @allure.story("Поиск фильмов")
    @allure.title("Поиск фильма по запросу")
    def test_search_movies(self, search_query, expected_text):
        self.main_page.open()
        with allure.step("Проверить строку поиска"):
            assert self.main_page.is_visible(MainPage.SEARCH_INPUT)
        with allure.step("Выполнить поиск"):
            self.main_page.search_movie(search_query)
        with allure.step("Проверить результаты"):
            assert self.main_page.is_visible(MainPage.SEARCH_RESULTS)
