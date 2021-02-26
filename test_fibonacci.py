import unittest
import fibonacci
import pytest

class TestCaseFibonacci(pytest.TestCase):


#testing some random number
      def test1(self):
        self.assertEqual(fibonacci.Fibonacci(9), 21)
