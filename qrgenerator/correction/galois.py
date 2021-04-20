class Galois:
    exponent = {0: 1}
    integer = {1: 0}

    def __init__(self):
        self.__gf(255)

    def __gf(self, end: int, start: int = 1, value: int = 1) -> int:
        value *= 2
        if value >= 256:
            value ^= 285

        self.exponent.update({start: value})
        if value not in self.integer.keys():
            self.integer.update({value: start})

        if start == end:
            return 0
        else:
            self.__gf(end, start + 1, value)

    def find_exponent(self, value: int):
        if 0 > value or value > 255:
            raise ValueError("Value needs to be within 0 and 255.")

        return self.integer.get(value)

    def find_integer(self, value: int):
        if 0 > value or value > 255:
            raise ValueError("Value needs to be within 0 and 255.")

        return self.exponent.get(value)
