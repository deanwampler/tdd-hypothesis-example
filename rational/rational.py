class Rational:
    """
    Represents rational numbers, a/b, where a and b are integers.
    For details, see https://en.wikipedia.org/wiki/Rational_number

    Raises a `ValueError` if the denominator is zero.
    """
    def __init__(self, numer: int, denom: int):
        if denom == 0:
            raise ValueError("Zero not allowed for the denominator!")
        self.numerator = numer
        self.denominator = denom

    def __eq__(self, other) -> bool:
        """
        a/b == c/d iff ad == bc
        """
        return self.numerator*other.denominator == self.denominator*other.numerator 
