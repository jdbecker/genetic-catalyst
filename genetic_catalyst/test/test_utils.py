from genetic_catalyst.utils import fibonacci, fibonacci_shift


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8


def test_fibonacci_shift():
    assert fibonacci_shift(1) == 1
    assert fibonacci_shift(2) == 2
    assert fibonacci_shift(3) == 3
    assert fibonacci_shift(4) == 5
    assert fibonacci_shift(5) == 8
    assert fibonacci_shift(6) == 13
