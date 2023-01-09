import pytest


def ids_a(val):
    return "a=({0})".format(str(val))


def ids_b(val):
    return "b=({0})".format(str(val))


def ids_c(val):
    return "c=({0})".format(str(val))


def is_triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        print("Длина стороны треугольника не может быть 0")
        return False
    elif a < 0 or b < 0 or c < 0:
        print("Длина стороны треугольника не может быть < 0")
        return False
    elif a + b > c:
        return True
    elif b + c > a:
        return True
    elif a + c > b:
        return True
    else:
        return False


@pytest.mark.parametrize("a", [-1, 0, 1, 2, 10], ids=ids_a)
@pytest.mark.parametrize("b", [-1, 0, 1, 2, 10], ids=ids_b)
@pytest.mark.parametrize("c", [-1, 0, 1, 2, 10], ids=ids_c)
def test_is_triangle(a, b, c):
    result = is_triangle(a, b, c)
    assert result == True
