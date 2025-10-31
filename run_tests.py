#!/usr/bin/env python3
import subprocess
import sys

def run_command(command, description):
    print(f"\n{'='*50}")
    print(f"Запуск: {description}")
    print(f"Команда: {command}")
    print('='*50)
    
    result = subprocess.run(command, shell=True)
    return result.returncode

def main():
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
    else:
        test_type = input("Выберите тип тестов (ui/api/all): ").strip().lower()
    
    if test_type == "ui":
        command = "pytest tests/test_ui.py -m ui -v --alluredir=allure-results"
        description = "UI тесты"
    elif test_type == "api":
        command = "pytest tests/test_api.py -m api -v --alluredir=allure-results"
        description = "API тесты"
    else:
        command = "pytest -v --alluredir=allure-results"
        description = "Все тесты"
    
    return_code = run_command(command, description)
    
    if return_code == 0:
        print(f"\n✅ {description} завершены успешно!")
    else:
        print(f"\n❌ {description} завершены с ошибками!")
    
    sys.exit(return_code)

if __name__ == "__main__":
    main()
