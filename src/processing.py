def filter_by_state(info_account: list, filter_of_sort: str = "EXECUTED") -> list:
    """фильтрует по state"""

    filtered_list = []
    if info_account == []:
        result = "Введен пустой список"
        raise KeyError(result)
    for list_of_workbooks in info_account:
        if list_of_workbooks["state"] == filter_of_sort:
            filtered_list.append(list_of_workbooks)
        elif list_of_workbooks["state"] == "":
            result = "В state не указано значение"
            raise KeyError(result)
    print(filtered_list)
    return filtered_list


def sort_by_date(info_account: list, key_to_sort: bool = True) -> list:
    """фильтрует по дате по убыванию"""
    if info_account == []:
        result = ["Введены неккоректные данные"]
        raise ValueError(result)
    else:
        info_account.sort(reverse=key_to_sort, key=lambda x: x["date"])
        print(info_account)
        return info_account
