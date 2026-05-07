import Lab2 as lab2

def test_minmax():
    result = []
    input_arr = [20, 30, 40, 50, 60]
    test_arr = (20, 60)

    result = lab2.minmax(input_arr)

    assert (result == test_arr)

def test_average():
    result = []
    input_arr = [20, 30, 40, 50, 60]
    test_arr = 40

    result = lab2.average(input_arr)

    assert (result == test_arr)

def test_median_odd():
    result = []
    input_arr = [20, 30, 40, 50, 60]
    test_arr = 40

    result = lab2.median(input_arr)

    assert (result == test_arr)

def test_median_even():
    result = []
    input_arr = [20, 30, 40, 50, 60, 70]
    test_arr = 45.0

    result = lab2.median(input_arr)

    assert (result == test_arr)