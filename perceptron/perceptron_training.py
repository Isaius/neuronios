# este programa treina uma rede neural perception simples
# código feito por Isaius

def potencial(x1, x2, w):
    # x1*w2 + x2*w2 - limiar
    return (x1*w[1] + x2*w[2]) - w[0] 

def g(u):
    # função de ativação degrau
    if u >= 0:
        return 1
    return 0

def recalibrar(w, tx, diff, x):
    for i in range(3):
        w[i] = w[i] + (tx*(diff)) * x[i]

print("Treinamento de rede perceptron")

qtd_amostras = int(input("Quantidade de amostras: "))

x1 = []
x2 = []
d = []
w = []

for i in range(qtd_amostras):
    x1.append(float(input("Valor " + str(i) + " de x1: ")))
    x2.append(float(input("Valor " + str(i) + " de x2: ")))
    d.append(float(input("Valor de saida esperado: ")))

print("Informe os parâmetros livres (vetor w): ")
w.append(float(input("Limiar inicial: ")))
w.append(float(input("Peso w1 inicial: ")))
w.append(float(input("Peso w2 inicial: ")))

tx_aprendizado = float(input("Informe a taxa de aprendizado: "))

epocas = 0
erro = True

while(erro):
    erro = False
    for i in range(qtd_amostras):
        x = [-1, x1[i], x2[i]]
        u = potencial(x[1], x[2], w)
        y = g(u)
        if y != d[i]:
            recalibrar(w, tx_aprendizado, d[i] - y, x)
            erro = True
    epocas += 1



