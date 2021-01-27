import re
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


class Polynomial:
    def __init__(self):
        self.equation = list()

    def __repr__(self):
        return f"Polynomial({' + '.join(map(str, self.equation))})"

    def __str__(self):
        return " + ".join(map(str, self.equation))

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_poly = Polynomial()
            new_poly.equation = self.__multiply_equations(self.equation, other.equation)
            return new_poly

    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            pass

    def __multiply_equations(self, equation_1: list, equation_2: list) -> list:
        mult_eq = list()
        for eq1 in equation_1:
            for eq2 in equation_2:
                mult_eq.append(eq1 * eq2)

        # TODO - Consolidate equation
        new_eq = list()
        for _ in range(mult_eq[0].exponent, -1, -1):
            coefficient = list(map(
                lambda x: x.coefficient,
                list(filter(lambda x: x.exponent == _, mult_eq))
            ))

            try:
                coefficient = coefficient[0] ^ coefficient[1]
            except IndexError:
                coefficient = coefficient[0]

            # coefficient = coefficient if coefficient < 256 else coefficient % 255
            new_eq.append(Term(coefficient, _))

        return new_eq


class Message(Polynomial):
    def __init__(self, encoded_string: str):
        super().__init__()
        self.equation = self.create_message_polynomial(encoded_string)

    def __repr__(self):
        return f"PloyMessage({self})"

    def create_message_polynomial(self, string: str):
        equation = []
        split_string = [string[x:x+8] for x in range(0, len(string), 8)]
        poly_length = len(split_string)
        for power, val in enumerate(split_string):
            equation.append(Term(int(val, 2), poly_length - (power + 1)))

        return equation


class Generator(Polynomial):
    generator_from_words = {2: [Term(1, 2), Term(3, 1), Term(2, 0)]}

    def __init__(self, code_words: int):
        super().__init__()
        self.equation = self.create_generator_polynomial(code_words)

    def __repr__(self):
        return f"PolyGenerator({self})"

    def create_generator_polynomial(self, words: int):
        if words in self.generator_from_words.keys():
            return self.generator_from_words[words]

        for num in range(3, words + 1):
            x = Polynomial()
            y = Polynomial()
            x.equation = self.generator_from_words[num - 1]
            y.equation = [Term(1, 1), Term(GF.find_integer(num), 0)]
            z = x * y
            self.generator_from_words.update({num: z.equation})

        return self.generator_from_words[words]
