from .galois import Galois
from .term import Term


GF = Galois()


class Polynomial:
    def __init__(self):
        self.equation: list[Term] = list()

    def __repr__(self) -> str:
        return f"Polynomial({' + '.join(map(str, self.equation))})"

    def __str__(self) -> str:
        return " + ".join(map(str, self.equation))

    def bin(self):
        coefficients = list(map(lambda x: x.coefficient, self.equation))
        return "".join(list(map(lambda x: bin(x)[2:].zfill(8), coefficients)))

    def copy(self):
        new = Polynomial()
        new.equation = self.equation.copy()
        return new

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_poly = Polynomial()
            new_poly.equation = self.__multiply_equations(self.equation, other.equation)
            return new_poly

    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            mul_poly = Polynomial()
            mul_poly.equation = [Term(1, other.equation[0].exponent)]
            new_poly = self * mul_poly
            gen_poly = other
            while new_poly.equation[-1].exponent != 0:
                new_poly = self.__divide_equations(new_poly, gen_poly)

            return new_poly

    def __divide_equations(self, poly_1, poly_2):
        mul_poly = Polynomial()
        mul_poly.equation = [
            Term(poly_1.equation[0].coefficient, poly_1.equation[0].exponent - poly_2.equation[0].exponent)
        ]
        poly_2 = poly_2 * mul_poly
        mul_poly.equation = list()
        length = len(poly_1.equation) if len(poly_1.equation) > len(poly_2.equation) else len(poly_2.equation)
        for _ in range(length):
            try:
                mul_poly.equation.append(poly_1.equation[_] / poly_2.equation[_])
            except IndexError:
                try:
                    mul_poly.equation.append(poly_1.equation[_])
                except IndexError:
                    mul_poly.equation.append(poly_2.equation[_])

        mul_poly.equation = mul_poly.equation[1:]
        return mul_poly

    def __multiply_equations(self, equation_1: list[Term], equation_2: list[Term]) -> list[Term]:
        mult_eq = list()
        for eq1 in equation_1:
            for eq2 in equation_2:
                mult_eq.append(eq1 * eq2)

        new_eq = list()
        for _ in range(mult_eq[0].exponent, -1, -1):
            coefficient = list(map(
                lambda x: x.coefficient,
                list(filter(lambda x: x.exponent == _, mult_eq))
            ))

            try:
                coefficient = coefficient[0] ^ coefficient[1]
                new_eq.append(Term(coefficient, _))
            except IndexError:
                try:
                    coefficient = coefficient[0]
                    new_eq.append(Term(coefficient, _))
                except IndexError:
                    pass

        return new_eq


class Message(Polynomial):
    def __init__(self, encoded_string: str):
        super().__init__()
        self.equation = self.create_message_polynomial(encoded_string)

    def __repr__(self) -> str:
        return f"PloyMessage({self})"

    def create_message_polynomial(self, string: str) -> list[Term]:
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

    def __repr__(self) -> str:
        return f"PolyGenerator({self})"

    def create_generator_polynomial(self, words: int) -> list[Term]:
        if words in self.generator_from_words.keys():
            return self.generator_from_words[words]

        for num in range(3, words + 1):
            x = Polynomial()
            y = Polynomial()
            x.equation = self.generator_from_words[num - 1]
            y.equation = [Term(1, 1), Term(GF.find_integer(num - 1), 0)]
            z = x * y
            self.generator_from_words.update({num: z.equation})

        return self.generator_from_words[words]
