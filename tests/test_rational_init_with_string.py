# Additional example unit tests using Hypothesis for property-based testing:
# Rational arithmetic.
# https://hypothesis.readthedocs.io/en/latest/

from hypothesis import given, strategies as st
import unittest
from rational import Rational, NonIntegerString
from test_utilities import nonzero_integers, nonzero_floats, non_int_strs

class TestRationalInitWithString(unittest.TestCase):
    """
    Test construction of Rationals using a string argument, "M/N".
    """

    @given(st.integers(), nonzero_integers)
    def test_from_str_takes_numerator_denominator_ints_as_strings(self, numer, denom):
        rat = Rational.from_str(str(numer), str(denom))
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denominator)

    @given(st.floats(), nonzero_integers)
    def test_from_str_raises_if_numerator_string_a_float(self, numer, denom):
        with self.assertRaises(NonIntegerString):
            rat = Rational.from_str(str(numer), str(denom))

    @given(st.integers(), nonzero_floats)
    def test_from_str_raises_if_denominator_string_a_float(self, numer, denom):
        with self.assertRaises(NonIntegerString):
            rat = Rational.from_str(str(numer), str(denom))

    # Potential bug: what if st.text() happens to return a valid integer string
    # occasionally? In fact, it does this often. So, this is why we use the 
    # non_int_strs strategy defined above.
    @given(non_int_strs, non_int_strs)
    def test_from_str_raises_if_other_non_int_strings_are_passed(self, numer_str, denom_str):
        with self.assertRaises(NonIntegerString):
            rat = Rational.from_str(numer_str, denom_str)
            print(f"Bad rat?? {rat}") # Seen occasionally, indicating non_int_strs isn't working completely reliably. TODO

if __name__ == "__main__":
    unittest.main()