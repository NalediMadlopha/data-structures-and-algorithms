


class MyMathClass:

    def __init__(self):
        self.p = 1

    def pow(self, x: int, y: int):
        if x == 1:
            print(x * y)
            return

        if self.p == 1:
            self.p = x

        if y > 1:
            self.pow(x * self.p, y - 1)
        else:
            print(x)

MyMathClass().pow(2, 10)
