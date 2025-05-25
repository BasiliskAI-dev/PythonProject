def filter_by_state(state=list, filter_of_sort='EXECUTED') -> list:
    filtered_list = []
    for list_of_workbooks in state:
        if list_of_workbooks['state'] == filter_of_sort:
            filtered_list.append(list_of_workbooks)
    print(filtered_list)
    return (filtered_list)


state = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

filter_by_state(state, "CANCELED")

