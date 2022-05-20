from sample.sum import sum_num


def test_sum_num():
    assert sum_num(3, 3) == 6


def test_sum_is_int():
    assert type(sum_num(2, 6)) is int


def test_sum_incorrect_result():
    assert sum_num(3, 4) != 8
