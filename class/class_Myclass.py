class Myclass:
    def __init__(self, x, x_weight=0.5):
        self.x = x
        self.x_weight = x_weight

    def __str__(self):
        return f"({self.x}::{self.x_weight})"

    def logical_and(self, other):
        if self.x == other.x:
            return Myclass(self.x, min(self.x_weight, other.x_weight))
        else:
            raise ValueError("x values are not equal")

    def logical_or(self, other):
        if self.x == other.x:
            return Myclass(self.x, max(self.x_weight, other.x_weight))
        else:
            raise ValueError("x values are not equal")

    def complement(self):
        complement_weight = round(1 - self.x_weight, 2)
        return Myclass(self.x, complement_weight)


def main():
    try:
        O1 = Myclass(5, 0.8)
        O2 = Myclass(5, 0.8)
        O3 = Myclass(7, 0.8)
        O4 = O1.logical_and(O2)
        print(O4)
        O5 = O1.logical_or(O2)
        print(O5)
        O6 = O3.complement()
        print(O6)
        O7 = O1.logical_and(O3)
        print(O7)
        O8 = O1.logical_or(O3)
        print(O8)
    except ValueError as msg:
        print(msg)


if __name__ == "__main__":
    main()
