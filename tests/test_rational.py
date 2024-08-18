# Example unit tests using Hypothesis for property-based testing.
# https://hypothesis.readthedocs.io/en/latest/

from hypothesis import given, strategies as st
import unittest
from rational import Rational
from test_utilities import nonzero_integers

class TestRational(unittest.TestCase):
    """
    Test the features implemented curently by Rational.
    Add new tests for Rational arithmetic operations, like multiplication and addition,
    watch the test fail, then implement the feature and ensure the test now passes.
    See also other properties described in the Rational Wikipedia page:
    https://en.wikipedia.org/wiki/Rational_number
    
    Also, try adding a second way to construct Rationals that accepts a string
    argument, "M/N". (Now you really have to think about handling input errors!) 
    What are the requirements for valid strings, e.g., for "M" and "N"?
    If an invalid string is provided, how should the error be handled?
    """

    @given(st.integers(), nonzero_integers)
    def test_init_takes_numerator_denominator(self, numer, denom):
        """
        A trivial test, but it gets us started.
        """
        rat = Rational(numer, denom)
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denominator)

    @given(st.integers())
    def test_zero_denominator_raises(self, numer):
        """
        Don't allow zero for the denominator!!
        """
        with self.assertRaises(ValueError):
            rat = Rational(numer, 0)

    @given(st.integers(), nonzero_integers)
    def test_a_rational_equals_itself(self, numer, denom):
        """
        This test passes without any code changes, e.g., adding a
        custom __eq__ method. Ask yourself, is this actually testing 
        instance equality or just locations in memory?
        """
        rat = Rational(numer, denom)
        self.assertEqual(rat, rat)

    @given(st.integers(), nonzero_integers)
    def test_identical_rationals_are_equal(self, numer, denom):
        """
        Would this one pass if we deleted (or commented out) our custom __eq__ method? 
        Try it!
        """
        rat1 = Rational(numer, denom)
        rat2 = Rational(numer, denom)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), nonzero_integers, nonzero_integers)
    def test_equality_for_two_rationals_with_num_and_dom_that_are_multiples_of_each_other(self, numer, denom, multiple):
        """
        Rule: a/b == c/d iff ad == bc
        Since a*M/b*M == a/b, then a*M/b*M == c/d
        """
        rat1 = Rational(numer*multiple, denom*multiple)
        rat2 = Rational(numer, denom)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), nonzero_integers, st.integers(), nonzero_integers)
    def test_equality_for_two_rationals_that_are_not_multiples_of_each_other(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b == c/d iff ad == bc
        This is a better test, because it randomly generates different instances.
        However, the text has to check for the case where the two values happen to be
        equivalent!
        """
        rat1 = Rational(numer1, denom1)
        rat2 = Rational(numer2, denom2)
        if numer1*denom2 == numer2*denom1:
            self.assertEqual(rat1, rat2)
        else:
            self.assertNotEqual(rat1, rat2)

if __name__ == "__main__":
    unittest.main()