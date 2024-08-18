# README tdd-hypothesis-example

Dean Wampler

This is a simple example used to demonstrate test-driven development in Python, but using _property-based testing_ as implemented by [`hypothesis`](https://hypothesis.readthedocs.io/en/latest/). As an example, [rational numbers](https://en.wikipedia.org/wiki/Rational_number) are used.

Run `make all` to install `hypothesis` and run the tests, which should pass.

Examine what features the tests are exploring and how they are implemented. Then try adding new tests and corresponding rational features, such as arithmetic operations.

To practice _test driven development_ (TDD), if you haven't done it before, begin by
adding a new test for some rational arithmetic operation that isn't yet implemented, like multiplication or addition. Then run the tests (`make test`) and watch the test fail. Now implement the feature in the `Rational` class and ensure the test now passes. Wash, rinse, repeat...

See also other properties described in the [rational Wikipedia page](https://en.wikipedia.org/wiki/Rational_number).

Also, try adding a second way to construct instances of `Rational` that accepts a string
argument, e.g., `"M/N"` for integers `M` and `N`. Now you really have to think about handling input errors! What are the requirements for valid `M` and `N` strings?
If an invalid string is provided, how should the error be handled?