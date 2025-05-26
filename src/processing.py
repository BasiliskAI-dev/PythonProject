def filter_by_state(info_account: list, filter_of_sort: str = "EXECUTED") -> list:
    """фильтрует по state"""

    filtered_list = []
    for list_of_workbooks in info_account:
        if list_of_workbooks["state"] == filter_of_sort:
            filtered_list.append(list_of_workbooks)
    print(filtered_list)
    return filtered_list


def sort_by_date(info_account: list, key_to_sort: bool = True) -> list:
    """фильтрует по дате по убыванию"""

    info_account.sort(reverse=key_to_sort, key=lambda x: x["date"])
    print(info_account)
    return info_account
