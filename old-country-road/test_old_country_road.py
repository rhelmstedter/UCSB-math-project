from old_country_road import _calc_cottage_distances, _calc_integral_distances


def test_distances():
    expected = (1, 1, 1, 1, 1, 22)
    actual = _calc_cottage_distances((0, 1, 2, 3, 4, 5))
    assert actual == expected


def test_known_good():
    expected = set(range(0, 27))
    actual = _calc_integral_distances((1, 1, 4, 4, 3, 14))
    assert actual == expected


def test_my_solution():
    expected = set(range(0, 27))
    actual = _calc_integral_distances((2, 1, 7, 8, 5, 4))
    assert actual == expected


def test_known_bad():
    missing_values = {4, 23, 13, 14}
    expected = set(range(0, 27)) - missing_values
    actual = _calc_integral_distances((1, 2, 3, 5, 7, 9))
    assert actual == expected
