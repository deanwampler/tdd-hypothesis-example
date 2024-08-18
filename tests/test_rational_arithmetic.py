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
    @given(st.integers(), nonzero_integers)
    def test_init_takes_numerator_denominator(self, numer, denom):
        """
        A trivial test, but it gets us started.
        """
        rat = Rational(numer, denom)
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denominator)

if __name__ == "__main__":
    unittest.main()