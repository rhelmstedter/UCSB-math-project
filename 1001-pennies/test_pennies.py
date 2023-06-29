from pennies import calc_coins


def test_total():
    actual = float(sum(calc_coins()))
    expected = 99.19
    assert actual == expected
