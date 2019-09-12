class MCP:
    w1 = 0
    w2 = 0
    w3 = 0
    limiar = 0

    def __init__(self, w1, w2, w3, limiar):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.limiar = limiar

    def calculate(self, x1, x2, x3):
        return ((((self.w1*x1) + (self.w2*x2)) + (self.w3*x3)) - self.limiar)

A = MCP(0.6, 0.7, 0, 0.1)
B = MCP(0.4, 0.2, 0, 0.8)
C = MCP(0.1, 0.3, 0, 0.5)
S = MCP(0.6, 0.5, 0.4, 0.2)

x1 = [0, 0, 0.25, 0.90, 0.55, 1.00, 0.14, 0.92, 0.26, 0.19]
x2 = [0, 0.25, 0.40, 0.30, 0.30, 1.00, 0,29, 0.19, 0.39, 0.78]

for i in range(10):
    result_a = A.calculate(x1[i], x2[i], 0)
    result_b = B.calculate(x1[i], x2[i], 0)
    result_c = C.calculate(x1[i], x2[i], 0)

    print("A: " + str(result_a))
    print("B: " + str(result_b))
    print("C: " + str(result_c))
    print("S: " + str(S.calculate(result_a, result_b, result_c)))
    print("\n")