imoprt re
from .galois import Galois


GF = Galois()


class Term:
    coefficient: int
    exponent: int
    variable: str = 'x'

    def __init__(self, coefficient: int, exponent: int):
        self.coefficient = coefficient
        self.exponent = exponent

    def __repr__(self):
        return f"Term({self.coefficient}, {self.exponent})"

    def __str__(self):
        superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        if self.coefficient == 1:
            if self.exponent == 0:
                coe = self.coefficient
            else:
                coe = ''
        else:
            coe = self.coefficient

        if self.exponent == 0:
            var = ''
            exp = ''
        elif self.exponent == 1:
            var = self.variable
            exp = ''
        else:
            var = self.variable
            exp = self.exponent

        return f"{coe}{var}{str(exp).translate(superscript)}"

    def __mul__(self, other):
        if isinstance(other, Term):
            x1 = GF.find_exponent(self.coefficient)
            y1 = GF.find_exponent(other.coefficient)
            z1 = x1 + y1
            if z1 >= 256:
                z1 = z1 % 255
            return Term(GF.find_integer(z1), self.exponent + other.exponent)

    def __gt__(self, other):
        if isinstance(other, Term):
            return self.exponent > other.exponent

    def __lt__(self, other):
        if isinstance(other, Term):
            return self.exponent < other.exponent

    @classmethod
    def create_from_str(cls, single_term: str):
        superscript = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
        groups = re.compile(r'(\d*)?([a-zA-Z])?(.*)?')
        terms = groups.findall(single_term)[0]

        return Term(
            (int(terms[0]) if terms[0] != '' else 1),
            (int(terms[2].translate(superscript)) if terms[2] != '' else 0)
        )
