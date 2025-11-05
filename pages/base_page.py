from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from config.constants import constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, constants.TIMEOUT)
        self.base_url = constants.KINOPOISK_URL

    @allure.step("Открыть страницу")
    def open(self, url=""):
        self.driver.get(f"{self.base_url}/{url.lstrip('/')}")

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст в элемент")
    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
