import requests
import allure
import json
from config.settings import settings


class KinopoiskAPIClient:
    def __init__(self):
        self.base_url = settings.KINOPOISK_API_URL
        self.headers = {
            "X-API-KEY": settings.API_KEY,
            "Content-Type": "application/json"
        }

    @allure.step("GET запрос к {endpoint}")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=settings.API_TIMEOUT
        )

        allure.attach(
            f"URL: {url}\nParams: {params}\nStatus: {response.status_code}",
            name="Request Details",
            attachment_type=allure.attachment_type.TEXT
        )

        try:
            response_data = response.json()
            allure.attach(
                json.dumps(response_data, ensure_ascii=False, indent=2),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON
            )
        except ValueError:
            allure.attach(
                response.text,
                name="Response Body",
                attachment_type=allure.attachment_type.TEXT
            )

        return response
