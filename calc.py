class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        self.num1 + n