# Utilities

from hypothesis import strategies as st
from utilities import check_int

# Disallow zero integers, e.g., for demoninators!
nonzero_integers = st.integers().filter(lambda i: i != 0)

# Disallow zero floats, e.g., for demoninators! Actually only used for tests where
# floats are rejected. Note that the comparison "f != 0.0" would not be useful for
# real float handling. Instead, you would want to check within a very small delta
# NEAR zero. However, for test purposes, it is okay as used.
nonzero_floats = st.floats().filter(lambda f: f != 0.0)

non_int_strs = st.text().filter(lambda s: not check_int(s))
