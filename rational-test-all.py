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
        self.denominator = denom

    def __eq__(self, other) -> bool:
        """
        a/b == c/d iff ad == bc
        """
        return self.numerator*other.denominator == self.denominator*other.numerator 

# Here are a number of tests after several iterations, with corresponding code above
# in Rational.
class TestEncoding(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_init_takes_numberator_denominator(self, numer, denom):
        """
        A trivial test, but it gets us started.
        """
        rat = Rational(numer, denom)
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denominator)

    @given(st.integers(), st.integers())
    def test_a_rational_equals_itself(self, numer, denom):
        """
        This test passes without any code changes, e.g., adding a
        custom __eq__ method. Ask yourself, is this actually testing 
        instance equality or just locations in memory?
        """
        rat = Rational(numer, denom)
        self.assertEqual(rat, rat)

    @given(st.integers(), st.integers())
    def test_identical_rationals_are_equal(self, numer, denom):
        """
        Does this one pass without a custom __eq__ implementation?
        """
        rat1 = Rational(numer, denom)
        rat2 = Rational(numer, denom)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), st.integers(), st.integers())
    def test_equality_for_two_rationals_that_are_multiples_of_each_other(self, numer, denom, multiple):
        """
        Rule: a/b == c/d iff ad == bc
        This is not a particular comprehensive test, because the two instances are always equal.
        """
        rat1 = Rational(numer, denom)
        rat2 = Rational(numer*multiple, denom*multiple)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), st.integers(), st.integers(), st.integers())
    def test_equality_for_two_rationals_that_are_not_multiples_of_each_other(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b == c/d iff ad == bc
        This is a better test, because it generates instances that may be equivalent or not.
        """
        rat1 = Rational(numer1, denom1)
        rat2 = Rational(numer2, denom2)
        if numer1*denom2 == numer2*denom1:
            self.assertEqual(rat1, rat2)
        else:
            self.assertNotEqual(rat1, rat2)

    # Your turn! Try writing tests and corresponding methods in Rational
    # for multiplication and addition. Try other properties described in
    # the Wikipedia page.
    # Try adding a second way to construct Rationals that accepts a string
    # argument, "M/N". Now you really have to think about error handling. 
    # What are the requirements for valid strings, e.g., for "M" and "N"?
    # If an invalid string is provided, how should the error be handled?

if __name__ == "__main__":
    unittest.main()