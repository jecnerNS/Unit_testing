from funciones import factorialR


def test_factorial():
    assert factorialR(5) == 120

def test_factorial_cero():
    assert factorialR(0) == 1