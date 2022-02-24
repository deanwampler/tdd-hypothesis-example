# README hypothesis-example

This is a simple example Dean used to demonstrate test-driven development in Python.

In particular, it uses [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) for
_property-based testing_.


1. Install the hypothesis library: `pip install hypothesis`.
2. Open `rational-test-start.py` in an editor. 
3. In a terminal (or IDE) run the tests: `python rational-test-start.py`. It will fail the first time.
4. In the editor, uncomment the starting definition for `Rational`.
5. Rerun the tests, which should now pass.
6. _One at a time_, copy over each additional test in `rational-test-all.py`.
7. Confirm the test fails (although at least one passes without code changes!).
8. Edit `Rational` to make the test pass. Look at the implementation in `rational-test-all.py` if you need help.
9. Make sure all the tests now pass.
10. Repeat! There are suggestions in `rational-test-all.py` for additional functionality you might right.

