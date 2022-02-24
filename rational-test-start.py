from hypothesis import given, strategies as st
import unittest

class TestEncoding(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_init_takes_numberator_denominator(self, numer, denom):
        rat = Rational(numer, denom)
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denomenator)


if __name__ == "__main__":
    unittest.main()