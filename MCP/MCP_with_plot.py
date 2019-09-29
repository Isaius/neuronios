import matplotlib.pyplot as plt

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
        
    def execute_in_range(self, init, finish, num_result):
        resultados = []
        i = init
        while i <= finish:
            potencial = i*self.w[1] - self.entradas[0][0]
            x = self.func(potencial)
            resultados.append(x)
            i += num_result
        
        return resultados

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

## PROGRAMA INICIA AQUI ##
print("MCP Generico")

n_amostras = 1
n_entradas = 1
entradas = []
w = []

for k in range(n_amostras+1):
    lista = []
    for l in range(n_entradas+1):
        lista.append(0)

    entradas.append(lista)
    
for s in range(n_entradas+1):
    w.append(0)

w[0] = -1 # "peso" para o limitar

for i in range(1, n_entradas+1):
    w[i] = float(input(("Insira o valor de W" + str(i) + "\n")))

entradas[0][0] = float(input("Insira o limiar\n"))

print("Informe a função de ativação:")
print("1 - Linear")
print("2 - Degrau")
print("3 - Degrau Bipolar")
print("4 - Logística")
print("5 - Tangente Hiperbólica")

func = 0

while func <1 or func>5:
    func = int(input())

print("Neuronio configurado.")

neuronio = MCP(entradas, w, None)

if func == 1:
    neuronio.setFunc(linear)
elif func == 2:
    neuronio.setFunc(degrau)
elif func == 3:
    neuronio.setFunc(degrau_bipolar)
elif func == 4:
    neuronio.setFunc(logistica)
elif func == 5:
    neuronio.setFunc(tan_hiper)


init = -3
finish = 3
num_result = (abs(init) + finish)/50
saidas = neuronio.execute_in_range(init, finish, num_result)

p = init
points = []
z = 0
while p <= finish:
    points.append(p)
    p += num_result

plt.plot(points, saidas)
plt.grid(True)
plt.show()