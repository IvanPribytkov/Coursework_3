import json

def mask_card_number(card_number):
    """
    Маскирует номер карты, оставляя только первые 6 цифр и последние 4 цифры, разделенные пробелом.

    :param card_number: Номер карты для маскировки.
    :type card_number: str
    :return: Маскированный номер карты.
    :rtype: str
    """
    first_part = card_number[-16:-10]
    last_part = card_number[-4:]
    masked_number = f"{first_part}******{last_part}"
    masked_number = ' '.join(masked_number[i * 4:(i + 1) * 4] for i in range(4))
    return masked_number

def mask_account_number(account_number):
    """
    Маскирует номер счета, оставляя только последние 4 цифры номера счета и добавляя '**' в начале.

    :param account_number: Номер счета для маскировки.
    :type account_number: str
    :return: Маскированный номер счета.
    :rtype: str
    """
    masked_number = '**' + account_number[-4:]
    return masked_number

def main():
    try:
        # Чтение данных из файла
        with open('operations.json', 'r') as file:
            operations = json.load(file)

        # Фильтрация и сортировка операций
        executed_operations = [operation for operation in operations if operation.get('state') == 'EXECUTED']
        sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

        # Вывод информации о последних 5 операциях
        for operation in sorted_operations:
            date = operation['date'][:10]
            date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
            description = operation['description']
            from_account = mask_card_number(operation.get('from', ''))
            to_account = mask_account_number(operation['to'])
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            print(f"Дата: {date}")
            print(f"Описание: {description}")
            if operation.get('from'):
                print(f"Откуда: {from_account}")
            print(f"Куда: {to_account}")
            print(f"Сумма: {amount} {currency}\n")

    except FileNotFoundError:
        print("Файл 'operations.json' не найден.")

if __name__ == "__main__":
    main()
