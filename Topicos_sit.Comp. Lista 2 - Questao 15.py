class MCP:
    w1 = 0.6
    w2 = 0.64
    limiar = 0.86

    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2

    def calculate(self, x1, x2):
        return (((self.w1*x1) + (self.w2*x2)) - self.limiar)

neuronio = MCP(0.6, 0.64)

print("1 " + str(neuronio.calculate(0, 0)))
print("2 " + str(neuronio.calculate(0, 0.25)))
print("3 " + str(neuronio.calculate(0.25, 0.40)))
print("4 " + str(neuronio.calculate(0.90, 0.30)))
print("5 " + str(neuronio.calculate(0.55, 0.30)))
print("6 " + str(neuronio.calculate(1.00, 1.00)))
print("7 " + str(neuronio.calculate(0.14, 0.29)))
print("8 " + str(neuronio.calculate(0.92, 0.19)))
print("9 " + str(neuronio.calculate(0.26, 0.39)))
print("10 " + str(neuronio.calculate(0.19, 0.78)))