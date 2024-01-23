import json
import pytest
from main import mask_card_number, mask_account_number

# Путь к файлу с данными для тестирования
DATA_FILE = 'operations.json'


# Подготовка данных для тестирования
@pytest.fixture
def sample_operations():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


# Тест маскирования номера карты
def test_mask_card_number():
    assert mask_card_number('2842878893689012') == '2842 87** **** 9012'


# Тест маскирования номера счета
def test_mask_account_number():
    assert mask_account_number('90424923579946435907') == '**5907'


# Тест функции main для обработки операций
def test_main(sample_operations, capsys):
    # Вызываем main() с подготовленными данными
    with open(DATA_FILE, 'w') as file:
        json.dump(sample_operations, file)

    import main
    main.main()

    # Проверяем, что вывод содержит ожидаемые строки
    captured = capsys.readouterr()
    assert 'Дата: 07.12.2019' in captured.out
    assert 'Описание: Перевод организации' in captured.out
    assert 'Откуда: 2842 87** **** 9012' in captured.out
    assert 'Куда: **3655' in captured.out  # Исправлено здесь
    assert 'Сумма: 48150.39 USD' in captured.out

if __name__ == "__main__":
    pytest.main([__file__])