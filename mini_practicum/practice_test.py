import practice

def test_power_neg1():
    #setup
    exponent = -1
    base = 3
    expected = "Undefined"

    #invoke
    actual = practice.power(base, exponent)

    #analyze
    assert actual == expected

def test_power_0():
    #setup
    exponent = 0
    base = 3
    expected = 1

    #invoke
    actual = practice.power(base, exponent)

    #analyze
    assert actual == expected

def test_power_1():
    #setup
    exponent = 1
    base = 3
    expected = 3

    #invoke
    actual = practice.power(base, exponent)

    #analyze
    assert actual == expected

def test_power_3():
    #setup
    exponent = 3
    base = 3
    expected = 27

    #invoke
    actual = practice.power(base, exponent)

    #analyze
    assert actual == expected

def test_power_2():
    #setup
    exponent = 2
    base = 3
    expected = 9

    #invoke
    actual = practice.power(base, exponent)

    #analyze
    assert actual == expected