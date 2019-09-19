# este programa treina uma rede neural perception simples
# código feito por Isaius

def potencial(x1, x2, w):
    # x1*w2 + x2*w2 - limiar
    print("\nCombinador linear")
    print("x1*w1: " + str(x1) + "*" + str(w[1]) + " = " +str(x1*w[1]))
    print("x2*w2: " + str(x2) + "*" + str(w[2]) + " = " +str(x2*w[2]))
    return round((x1*w[1] + x2*w[2]) - w[0], 2)

def g(u):
    # função de ativação degrau
    if u >= 0:
        return 1
    return 0

def recalibrar(w, tx, diff, x):
    print("Recalibrando")
    for i in range(3):
        print("w" + str(i) + ": " + str(w[i]) + " + (" + str(tx) + "*" +str(diff) + ")*" + str(x[i]), end=" ")
        w[i] = round(w[i] + (tx*(diff)) * x[i], 2)
        print("= " + str(w[i]))

print("Treinamento de rede perceptron")

qtd_amostras = int(input("Quantidade de amostras: "))

x1 = []
x2 = []
d = []
w = []

print("Insira os valores das amostras")
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
    print("\n\nEpoca " + str(epocas))
    erro = False
    for i in range(qtd_amostras):
        x = [-1, x1[i], x2[i]]
        print("\nAmostra " + str(x[1]) + " " + str(x[2]))
        print("Limiar: " + str(w[0]) + " w1: " + str(w[1]) + " w2: " + str(w[2]))
        u = potencial(x[1], x[2], w)
        y = g(u)
        print("Potencial: " + str(u) + "\nSaida: " + str(y) + "\tEsperado: " + str(d[i]))
        if y != d[i]:
            print("\nErro para a amostra " + str(x))
            recalibrar(w, tx_aprendizado, d[i] - y, x)
            erro = True
    epocas += 1
print("\nRede Perceptron treinada")
print("\nParâmetros livres finais:\nw1: " + str(w[1]) + "\tw2: " + str(w[2]) + "\tLimiar: " + str(w[0]))


