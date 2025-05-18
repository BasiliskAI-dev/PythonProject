def get_mask_card_number(full_name: str) -> str:
    """Принимает номер карты, вовращает номер карты со скрытыми числами"""
    card_numbers=full_name[-16:]
    card_letters=full_name[:-16]
    card_number_hidden = ""
    for number in range(0, len(card_numbers), 4):
        card_number_hidden += card_numbers[number : number + 4] + " "
    result = card_letters + card_number_hidden[0:7] + "** **** " + card_number_hidden[-5:]
    print(result)

    return result


def get_mask_account(full_name: str) -> str:
    """Принимает номер аккаунта, возвращает номер аккаунта со
    скрытыми цифарами"""
    account_numbers = full_name[-4:]
    account_letters = full_name[:-20]
    result = account_letters + "**" + account_numbers[-4:]
    print(result)

    return result


