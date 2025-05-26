class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10, 20, 30))
