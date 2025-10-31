import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    KINOPOISK_URL = "https://www.kinopoisk.ru"
    KINOPOISK_API_URL = "https://kinopoiskapiunofficial.tech"
    API_KEY = os.getenv("API_KEY", "31d0851a-ad5b-4e73-8e2b-c274753f6263")
    TEST_EMAIL = os.getenv("TEST_EMAIL", "test@kinopoisk.ru")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "Test1234")
    TEST_MOVIE_TITLE = "Интерстеллар"
    TEST_MOVIE_FRAGMENT = "брат"
    TEST_MOVIE_ID = 301
    TEST_PERSON_ID = 63859
    INVALID_MOVIE_ID = 999999
    TIMEOUT = 10
    API_TIMEOUT = 30


settings = Settings()
