import pytest
import allure
from config.constants import constants


@allure.feature("API Тесты Кинопоиска")
@pytest.mark.api
class TestKinopoiskAPI:
    @allure.story("Поиск фильмов")
    @allure.title("API: Поиск фильма по ключевому слову 'брат'")
    def test_search_movie_by_keyword(self, api_client):
        with allure.step("Выполнить поиск"):
            response = api_client.get(
                "/api/v2.1/films/search-by-keyword",
                params={"keyword": "брат", "page": 1}
            )
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200, "Expected 200"
        with allure.step("Проверить структуру ответа"):
            data = response.json()
            assert "films" in data, "No 'films' key"
            assert len(data["films"]) > 0, "No films found"
        with allure.step("Проверить содержание"):
            first_film = data["films"][0]
            name_ru = first_film.get("nameRu", "")
            name_en = first_film.get("nameEn", "")
            film_name = name_ru or name_en
            assert "брат" in film_name.lower(), "Search word not found"

    @allure.story("Информация о фильмах")
    @allure.title("API: Получение карточки фильма 'Матрица' по ID")
    def test_get_movie_by_id(self, api_client):
        with allure.step("Получить информацию о фильме"):
            url = f"/api/v2.1/films/{constants.TEST_MOVIE_ID}"
            response = api_client.get(url)
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200, "Expected 200"
        with allure.step("Проверить данные фильма"):
            data = response.json()
            film_data = data.get("data", {})
            film_name = film_data.get("nameRu", "wrong_name")
            expected = "Матрица"
            msg = f"Expected '{expected}', got '{film_name}'"
            assert film_name == expected, msg

    @allure.story("Топ фильмы")
    @allure.title("API: Получение топа популярных фильмов")
    def test_get_top_popular_movies(self, api_client):
        with allure.step("Получить топ популярных фильмов"):
            response = api_client.get(
                "/api/v2.1/films/top",
                params={"type": "TOP_100_POPULAR_FILMS", "page": 1}
            )
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200, "Expected 200"
        with allure.step("Проверить наличие данных"):
            data = response.json()
            assert "films" in data, "No 'films' key"
            assert len(data["films"]) > 0, "No films found"

    @allure.story("Информация о персонах")
    @allure.title("API: Получение информации о персоне")
    def test_get_person_info(self, api_client):
        with allure.step("Получить информацию о персоне"):
            url = f"/api/v1/staff/{constants.TEST_PERSON_ID}"
            response = api_client.get(url)
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200, "Expected 200"
        with allure.step("Проверить данные персоны"):
            data = response.json()
            assert "nameRu" in data, "No 'nameRu' key"
            person_name = data["nameRu"]
            assert person_name, "Person name is empty"

    @allure.story("Обработка ошибок")
    @allure.title("API: Проверка обработки несуществующего фильма")
    def test_nonexistent_movie_handling(self, api_client):
        with allure.step("Запросить несуществующий фильм"):
            url = f"/api/v2.1/films/{constants.INVALID_MOVIE_ID}"
            response = api_client.get(url)
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 404, "Expected 404"
        with allure.step("Проверить тело ответа"):
            data = response.json()
            assert not data.get("data"), "Data should be empty"


@pytest.mark.api
class TestKinopoiskAdditionalAPI:
    @allure.story("Обработка ошибок")
    @allure.title("API: Проверка с невалидным API ключом")
    def test_invalid_api_key(self, api_client):
        api_client.headers["X-API-KEY"] = "INVALID_TEST_KEY"
        with allure.step("Выполнить запрос"):
            response = api_client.get("/api/v2.2/films/301")
        with allure.step("Проверить ответ"):
            assert response.status_code == 401, "Expected 401"
