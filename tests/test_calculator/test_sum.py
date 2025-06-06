from calculator.sum import sum


def test_sum():
    assert sum(5, 7) == 12
    assert sum(1, 1) == 2
