from netcovapp.services.location_tools import lambert93_to_gps, string_to_city


def test_lambert93_to_gps():
    x = 102980
    y = 6847973
    assert lambert93_to_gps(x, y) == (48.4565745588153, -5.0888561153013425)


def test_string_to_location():
    q = '42 rue 75011 Paris'
    assert string_to_city(q) == "Paris"

