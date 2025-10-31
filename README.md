# Автоматизированные тесты для Кинопоиска

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15.0-green)
![Pytest](https://img.shields.io/badge/Pytest-7.4.3-orange)
![Allure](https://img.shields.io/badge/Allure-2.13.2-red)

Проект содержит автоматизированные UI и API тесты для веб-приложения Кинопоиск, созданные в рамках финального задания курса.

## 📋 Ссылки

- **Репозиторий проекта**: [https://github.com/Guykavert/lesson-11-PN-Final-tests](https://github.com/Guykavert/lesson-11-PN-Final-tests)
- **Исходный проект ручного тестирования**: [ссылка на ваш финальный проект ручного тестирования]

## 🏗️ Структура проекта
kinopoisk-autotests/
├── config/ # Конфигурационные файлы
│ └── settings.py
├── pages/ # Page Object модели
│ ├── base_page.py
│ └── main_page.py
├── tests/ # Тесты (UI и API)
│ ├── test_ui.py
│ └── test_api.py
├── utils/ # Вспомогательные утилиты
│ └── api_client.py
├── requirements.txt # Зависимости
├── pytest.ini # Конфигурация pytest
├── conftest.py # Фикстуры pytest
└── README.md # Документация

## ⚙️ Установка и настройка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/Guykavert/lesson-11-PN-Final-tests.git
cd lesson-11-PN-Final-tests
Установите зависимости:
pip install -r requirements.txt
Запуск всех тестов
bash
pytest
Запуск только UI тестов
bash
pytest tests/test_ui.py -m ui
Запуск только API тестов
bash
pytest tests/test_api.py -m api
Запуск с генерацией Allure отчета
bash
pytest --alluredir=allure-results
allure serve allure-results
