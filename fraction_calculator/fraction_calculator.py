# !/usr/bin/env python3

from math import gcd


def main():
    try:
        f1 = Fraction(*list(map(int, input("Input first fraction:  ").split('/'))))
        f2 = Fraction(*list(map(int, input("Input second fraction:  ").split('/'))))
    except SyntaxError:
        print("Denominator cannot be zero")
        exit()
    operation = str(input("Choose one operation + - / * :  "))
    if operation == "+":
        f3 = Fraction.__add__(f1, f2)
        print(Fraction.__str__(f3))
    if operation == "-":
        f3 = Fraction.__sub__(f1, f2)
        print(Fraction.__str__(f3))
    if operation == "/":
        f3 = Fraction.__mul__(f1, f2)
        print(Fraction.__str__(f3))
    if operation == "*":
        f3 = Fraction.__truediv__(f1, f2)
        print(Fraction.__str__(f3))


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        if int(bottom) == 0:
            raise SyntaxError()
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)


if __name__ == "__main__":
    main()
