dict_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "NOT-EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

dict_2 = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]

testdata_1 = [
    (dict_1, dict_2),
]


test_state_input_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

test_state_output_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
test_state_input_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

test_state_output_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

testdata_2 = [
    (test_state_input_1, test_state_output_1),
    (test_state_input_2, test_state_output_2),
]

testdata_3 = [
    {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
]
