import os
from dotenv import load_dotenv

load_dotenv()


class Constants:
    KINOPOISK_URL = "https://www.kinopoisk.ru"
    KINOPOISK_API_URL = "https://kinopoiskapiunofficial.tech"
    API_KEY = os.getenv("API_KEY")
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
    TEST_MOVIE_TITLE = "Интерстеллар"
    TEST_MOVIE_FRAGMENT = "брат"
    TEST_MOVIE_ID = 301
    TEST_PERSON_ID = 63859
    INVALID_MOVIE_ID = 999999
    TIMEOUT = 10
    API_TIMEOUT = 30


constants = Constants()
