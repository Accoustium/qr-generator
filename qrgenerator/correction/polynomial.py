import re
# from .galois import Galois


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
        coe = self.coefficient if self.coefficient != 1 else ''

        var = self.variable if self.exponent != 0 else ''
        exp = self.exponent if self.exponent != 0 else ''

        return f"{coe}{var}{str(exp).translate(superscript)}"

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
        return f"Polynomial()"

    def __str__(self):
        return " + ".join(map(str, self.equation))


class Message(Polynomial):
    def __init__(self, encoded_string: str):
        super().__init__()
        self.equation = self.create_message_polynomial(encoded_string)

    def __repr__(self):
        return f"PloyMessage()"

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

    def __repr__(self):
        return f"PolyGenerator()"

    def create_generator_polynomial(self, words: int):
        pass
