# Example unit tests using Hypothesis for property-based testing.
# https://hypothesis.readthedocs.io/en/latest/

from hypothesis import given, strategies as st
import unittest

class Rational:
    """
    Represents rational numbers, a/b, where a and b are integers.
    For details, see https://en.wikipedia.org/wiki/Rational_number
    """
    def __init__(self, numer: int, denom: int):
        self.numerator = numer
        self.denomenator = denom

    def __eq__(self, other) -> bool:
        """
        a/b == c/d iff ad == bc
        """
        return self.numerator*other.denomenator == self.denomenator*other.numerator 

class TestEncoding(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_init_takes_numberator_denominator(self, numer, denom):
        rat = Rational(numer, denom)
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denomenator)

    @given(st.integers(), st.integers())
    def test_a_rational_equals_itself(self, numer, denom):
        rat = Rational(numer, denom)
        self.assertEqual(rat, rat)

    @given(st.integers(), st.integers(), st.integers())
    def test_equality_for_two_rationals_that_are_multiples_of_each_other(self, numer, denom, multiple):
        rat1 = Rational(numer, denom)
        rat2 = Rational(numer*multiple, denom*multiple)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), st.integers(), st.integers(), st.integers())
    def test_equality_for_two_rationals_that_are_not_multiples_of_each_other(self, numer1, denom1, numer2, denom2):
        """
        a/b == c/d  iff ad == bc
        """
        rat1 = Rational(numer1, denom1)
        rat2 = Rational(numer2, denom2)
        if numer1*denom2 == numer2*denom1:
            self.assertEqual(rat1, rat2)
        else:
            self.assertNotEqual(rat1, rat2)

    # Try writing tests and implementations for multiplication and addition of rationals.

if __name__ == "__main__":
    unittest.main()