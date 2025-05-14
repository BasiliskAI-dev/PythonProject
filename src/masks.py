def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты, вовращает номер карты со скрытыми числами"""
    card_number_str = str(card_number)
    card_number_hidden = ""
    for number in range(0, len(card_number_str), 4):
        card_number_hidden += card_number_str[number : number + 4] + " "
    result = card_number_hidden[0:7] + "** **** " + card_number_hidden[-5:]
    print(result)

    return result


def get_mask_account(account_number: int) -> str:
    """Принимает номер аккаунта, возвращает номер аккаунта со
    скрытыми цифарами"""
    account_number_str = str(account_number)
    result = "**" + account_number_str[-4:]
    print(result)
    return result
