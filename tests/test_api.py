import pytest
import allure
from utils.api_client import KinopoiskAPIClient
from config.settings import settings


@allure.feature("API Тесты Кинопоиска")
@pytest.mark.api
class TestKinopoiskAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = KinopoiskAPIClient()

    @allure.story("Поиск фильмов")
    @allure.title("API: Поиск фильма по ключевому слову 'брат'")
    def test_search_movie_by_keyword(self):
        with allure.step("Выполнить поиск по ключевому слову 'брат'"):
            response = self.api_client.get(
                "/api/v2.1/films/search-by-keyword",
                params={"keyword": "брат", "page": 1}
            )
        with allure.step("Проверить успешный статус ответа"):
            assert response.status_code == 200
        with allure.step("Проверить структуру ответа"):
            data = response.json()
            assert "films" in data
            assert len(data["films"]) > 0

    @allure.story("Информация о фильмах")
    @allure.title("API: Получение карточки фильма 'Матрица' по ID")
    def test_get_movie_by_id(self):
        with allure.step("Получить информацию о фильме по ID"):
            response = self.api_client.get(
                f"/api/v2.1/films/{settings.TEST_MOVIE_ID}"
            )
        with allure.step("Проверить успешный статус ответа"):
            assert response.status_code == 200
        with allure.step("Проверить данные фильма"):
            data = response.json()
            assert "data" in data
            film_data = data["data"]
            assert film_data.get("nameRu") == "Матрица"

    @allure.story("Топ фильмы")
    @allure.title("API: Получение топа популярных фильмов")
    def test_get_top_popular_movies(self):
        with allure.step("Получить топ популярных фильмов"):
            response = self.api_client.get(
                "/api/v2.1/films/top",
                params={"type": "TOP_100_POPULAR_FILMS", "page": 1}
            )
        with allure.step("Проверить успешный статус ответа"):
            assert response.status_code == 200
        with allure.step("Проверить наличие данных"):
            data = response.json()
            assert "films" in data
            assert len(data["films"]) > 0

    @allure.story("Информация о персонах")
    @allure.title("API: Получение информации о персоне")
    def test_get_person_info(self):
        with allure.step("Получить информацию о персоне"):
            response = self.api_client.get(
                f"/api/v1/staff/{settings.TEST_PERSON_ID}"
            )
        with allure.step("Проверить успешный статус ответа"):
            assert response.status_code == 200
        with allure.step("Проверить данные персоны"):
            data = response.json()
            assert "nameRu" in data

    @allure.story("Обработка ошибок")
    @allure.title("API: Проверка обработки несуществующего фильма")
    def test_nonexistent_movie_handling(self):
        with allure.step("Запросить несуществующий фильм"):
            response = self.api_client.get(
                f"/api/v2.1/films/{settings.INVALID_MOVIE_ID}"
            )
        with allure.step("Проверить ответ сервера"):
            assert response.status_code in [200, 404]


@pytest.mark.api
class TestKinopoiskAdditionalAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = KinopoiskAPIClient()

    @allure.story("Обработка ошибок")
    @allure.title("API: Проверка с невалидным API ключом")
    def test_invalid_api_key(self):
        invalid_client = KinopoiskAPIClient()
        invalid_client.headers["X-API-KEY"] = "INVALID_TEST_KEY"
        with allure.step("Выполнить запрос с невалидным ключом"):
            response = invalid_client.get("/api/v2.2/films/301")
        with allure.step("Проверить ответ об ошибке"):
            assert response.status_code in [401, 403]
