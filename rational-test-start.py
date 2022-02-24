# Example unit tests using Hypothesis for property-based testing.
# https://hypothesis.readthedocs.io/en/latest/

from hypothesis import given, strategies as st
import unittest

# FIRST run this test (python rational-test-start.py), which will fail.
# THEN uncomment the following to start defining Rational. The test should pass.
# class Rational:
#     """
#     Represents rational numbers, a/b, where a and b are integers.
#     """
#     def __init__(self, numer: int, denom: int):
#         self.numerator = numer
#         self.denominator = denom

#     def __eq__(self, other) -> bool:
#         return self.numerator*other.denominator == other.numerator*self.denominator

class TestEncoding(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_init_takes_numberator_denominator(self, numer, denom):
        """
        A trivial test, but it gets us started.
        """
        rat = Rational(numer, denom)
        self.assertEqual(numer, rat.numerator)
        self.assertEqual(denom, rat.denominator)

    # Look at rational-test-all.py for more tests. Copy over one test at a time, 
    # confirm the test fails (or not in a few cases!), then write the additional
    # code in Rational required to make the new test pass. Iterate...
    
if __name__ == "__main__":
    unittest.main()