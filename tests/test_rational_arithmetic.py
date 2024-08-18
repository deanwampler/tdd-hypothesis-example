# Additional example unit tests using Hypothesis for property-based testing:
# Rational arithmetic.
# https://hypothesis.readthedocs.io/en/latest/

from hypothesis import given, strategies as st
import unittest
from rational import Rational
from test_utilities import nonzero_integers

class TestRationalArithmetic(unittest.TestCase):
    """
    Test operations like comparisons, addition, multiplication, etc.
    """
    @given(st.integers(), nonzero_integers, st.integers(), nonzero_integers)
    def test_comparison_of_two_rationals(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b < c/d iff ad < bc
        """
        rat1 = Rational(numer1, denom1)
        rat2 = Rational(numer2, denom2)
        if numer1*denom2 < numer2*denom1:
            self.assertLess(rat1, rat2)
        elif numer1*denom2 > numer2*denom1:
            self.assertGreater(rat1, rat2)
        else:
            self.assertLessEqual(rat1, rat2)
            self.assertGreaterEqual(rat1, rat2)

    @given(st.integers(), nonzero_integers, st.integers(), nonzero_integers)
    def test_addition_of_two_rationals(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b + c/d == (ad + bc) / bd
        """
        rat1   = Rational(numer1, denom1)
        rat2   = Rational(numer2, denom2)
        rat1p2 = rat1 + rat2
        adpbc  = rat1.numerator*rat2.denominator + rat2.numerator*rat1.denominator
        expected = Rational(adpbc, rat1.denominator*rat2.denominator)
        self.assertEqual(rat1p2, expected)

    @given(st.integers(), nonzero_integers, st.integers(), nonzero_integers)
    def test_subtraction_of_two_rationals(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b + c/d == (ad + bc) / bd
        """
        rat1   = Rational(numer1, denom1)
        rat2   = Rational(numer2, denom2)
        rat1m2 = rat1 - rat2
        admbc  = rat1.numerator*rat2.denominator - rat2.numerator*rat1.denominator
        expected = Rational(admbc, rat1.denominator*rat2.denominator)
        self.assertEqual(rat1m2, expected)

    @given(st.integers(), nonzero_integers, st.integers(), nonzero_integers)
    def test_multiplication_of_two_rationals(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b * c/d == ac / bd
        """
        rat1   = Rational(numer1, denom1)
        rat2   = Rational(numer2, denom2)
        rat1m2 = rat1 * rat2
        expected = Rational(rat1.numerator*rat2.numerator, rat1.denominator * rat2.denominator)
        self.assertEqual(rat1m2, expected)
        
if __name__ == "__main__":
    unittest.main()