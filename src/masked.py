from os import getcwd


def get_mask_card_number(full_name: str) -> str:
    """Принимает номер карты, возвращает номер карты со скрытыми числами"""
    card_letters = full_name[:-16]
    card_numbers=''
    for item in full_name:
        if item.isdigit():
            card_numbers += item
    if len(card_numbers) != 16:
        result = 'Введен некорректный номер карты'
        print(result)
    else:
        card_number_hidden = ""
        for number in range(0, len(card_numbers), 4):
            card_number_hidden += card_numbers[number: number + 4] + " "
        result = card_letters + card_number_hidden[0:7] + "** **** " + card_number_hidden[-5:]
        print(result)

    return result


def get_mask_account(full_name: str) -> str:
    """Принимает номер аккаунта, возвращает номер аккаунта со
    скрытыми цифрами"""
    account_number = ''
    for item in full_name:
        if item.isdigit():
            account_number += item
    if len(account_number) != 20:
        result = "Введен некорректный номер аккаунта"
        print(result)
    else:
        account_letters = full_name[:-20]
        result = account_letters + "**" + account_number[-4:]
        print(result)

    return result

