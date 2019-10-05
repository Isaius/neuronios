class MCP:
    def __init__(self, entradas, w, g):
        self.qnt_amostras = len(entradas)-1
        self.n_entradas = len(entradas[1])
        self.entradas = entradas
        self.w = w
        self.func = g
    
    def setFunc(self, func):
        self.func = func
    
    def setEntradas(self, entradas):
        self.qnt_amostras = len(entradas)
        self.n_entradas = len(entradas[0])
        self.entradas = entradas
    
    def execute(self):
        saidas = []
        for i in range(1, self.qnt_amostras+1):
            print("Amostra " + str(i))
            potencial = 0
            for j in range(1, self.n_entradas+1):
                # entradas[i][j] j é o valor de xi de 1 até n
                # pois x0 é o limiar. e w[j] de 1 até n pq w[0] é -1
                potencial += self.entradas[i][j-1]*self.w[j]
                print("X" + str(j) +"*W" +str(j) +": " + str(self.entradas[i][j-1]) + "*" + str(self.w[j]))
            potencial -= self.entradas[0][0]
            print("Potencial: " + str(potencial))
            y = self.func(potencial)
            saidas.append(y)
            print("Saida: " + str(y))
        return saidas

def linear(potencial):
    return potencial

def degrau(potencial):
    if potencial >= 0:
        return 1
    return 0

def degrau_bipolar(potencial):
    if potencial>= 0:
        return 1
    return -1

def logistica(potencial):
    return 1/(1 + (2.72**((-1)*(potencial-0.5))))

def tan_hiper(potencial):
    return (1 - (2.72**((-1)*potencial)))/(1 + (2.72**((-1)*potencial)))