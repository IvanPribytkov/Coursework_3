import json

def mask_card_number(card_number):
    """
    Маскирует номер карты, оставляя только первые 6 цифр и последние 4 цифры, разделенные пробелом.

    :param card_number: Номер карты для маскировки.
    :type card_number: str
    :return: Маскированный номер карты.
    :rtype: str
    """
    # Извлекаем первые 6 цифр и последние 4 цифры номера карты
    first_part = card_number[-16:-10]
    last_part = card_number[-4:]
    # Маскируем остальные цифры
    masked_number = f"{first_part}******{last_part}"
    return masked_number

def mask_account_number(account_number):
    """
    Маскирует номер счета, оставляя только последние 4 цифры номера счета и добавляя '**' в начале.

    :param account_number: Номер счета для маскировки.
    :type account_number: str
    :return: Маскированный номер счета.
    :rtype: str
    """
    # Извлекаем последние 4 цифры номера счета и добавляем '**' в начале
    masked_number = '**' + account_number[-4:]
    return masked_number

def main():
    # Чтение данных из файла
    with open('operations.json', 'r') as file:
        operations = json.load(file)

    # Фильтрация и сортировка операций
    # Фильтруем операции с проверкой наличия ключа 'state' и его значения 'EXECUTED'
    executed_operations = [operation for operation in operations if operation.get('state') == 'EXECUTED']
    # Сортировка по дате в убывающем порядке и выбор последних 5 операций
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    # Вывод информации о последних 5 операциях
    for operation in sorted_operations:
        # Извлекаем только дату из строки даты и времени
        date = operation['date'][:10]
        # Извлекаем описание операции
        description = operation['description']
        # Маскируем номер карты или счета, если они присутствуют
        from_account = mask_card_number(operation.get('from', ''))
        to_account = mask_account_number(operation['to'])
        # Извлекаем сумму и валюту операции
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        # Форматированный вывод информации о операции
        print(f"Дата: {date}")
        print(f"Описание: {description}")
        # Выводим маскированные номера карты или счета
        print(f"Откуда: {from_account} -> Куда: {to_account}")
        print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()
