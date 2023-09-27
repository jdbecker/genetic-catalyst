from django.test import TestCase
from creatures.utils import fibonacci, fibonacci_shift


class UtilTests(TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_shift(self):
        self.assertEqual(fibonacci_shift(1), 1)
        self.assertEqual(fibonacci_shift(2), 2)
        self.assertEqual(fibonacci_shift(3), 3)
        self.assertEqual(fibonacci_shift(4), 5)
        self.assertEqual(fibonacci_shift(5), 8)
        self.assertEqual(fibonacci_shift(6), 13)
