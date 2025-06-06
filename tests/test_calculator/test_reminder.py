from calculator.reminder import reminder


def test_reminder():
    assert reminder(5, 4) == 1
    assert reminder(4, 2) == 0
