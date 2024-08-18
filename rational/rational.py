from utilities import check_int

class NonIntegerString(ValueError):
    def __init__(self, msg: str):
        super().__init__(msg)

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

    @classmethod
    def from_str(toss, numer_str: str, denom_str: str):
        errors=[]
        if not check_int(numer_str):
            errors.append(f"Input string for numerator, '{numer_str}', is not an integer.")
        if not check_int(denom_str):
            errors.append(f"Input string for denominator, '{denom_str}', is not an integer.")
        if len(errors) > 0:
            raise NonIntegerString(" ".join(errors))

        return Rational(int(numer_str), int(denom_str))

    def __eq__(self, other) -> bool:
        """
        a/b == c/d iff ad == bc
        """
        return self.numerator*other.denominator == self.denominator*other.numerator 

    # def __lt__(self, other) -> bool:
    #     """
    #     a/b < c/d iff ad < bc
    #     """
    #     return self.numerator*other.denominator < self.denominator*other.numerator 
