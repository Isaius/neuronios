# este programa treina uma rede neural perception simples
# código feito por Isaius
import random
from math import sqrt, pow

def potencial(x1, x2, x3, w):
    # x1*w2 + x2*w2 + x3*w3- limiar
    return round((x1*w[1] + x2*w[2] + x3*w[3]) - w[0], 4)

def g(u):
    # função de ativação degrau
    if u >= 0:
        return 1
    return -1

def recalibrar(w, tx, diff, x):
    for i in range(4):
        w[i] = round(w[i] + (tx*(diff)) * x[i], 4)

def normalize(entrada):
    media = 0
    for i in entrada:
        media += i
    media = media/len(entrada)

    variancia = 0
    for i in entrada:
        variancia += pow(i - media, 2)

    variancia = variancia/len(entrada)
    desv_padrao = sqrt(variancia)

    normalizado = []
    for i in entrada:
        normalizado.append((i - media)/desv_padrao)
    
    return normalizado

print("Treinamento de rede perceptron")

qtd_amostras = 30

x1 = [-0.6508,-1.4492,2.0850,0.2626,0.6418,0.2569,1.1155,0.0914
        ,0.0121,-0.0429,0.4340,0.2735,0.4839,0.4089,1.4391,-0.9115
        ,0.3654,0.2144,0.2013,0.6483,-0.1147,-0.7970,-1.0625,0.5307
        ,-1.2200,0.3957,-0.1013,2.4482,2.0149,0.2012]

x2 = [0.1097,0.8896,0.6876,1.1476,1.0234,0.6730,0.6043,0.3399
        ,0.5256,0.4660,0.6870,1.0287,0.4851,-0.1267,0.1614,-0.1973
        ,1.0475,0.7515,1.0014,0.2183,0.2242,0.8795,0.6366,0.1285
        ,0.7777,0.1076,0.5989,0.9455,0.6192,0.2611]

x3 = [4.0009,4.4005,12.0710,7.7985,7.0427,8.3265,7.4446,7.0677
        ,4.6316,5.4323,8.2287,7.1934,7.4850,5.5019,8.5843,2.1962
        ,7.4858,7.1699,6.5489,5.8991,7.2435,3.8762,2.4707,5.6883
        ,1.7252,5.6623,7.1812,11.2095,10.9263,5.4631]

d = [-1.0000,-1.0000,-1.0000,1.0000,1.0000,-1.0000,1.0000,-1.0000
        ,1.0000,1.0000,-1.0000,1.0000,-1.0000,-1.0000,-1.0000,-1.0000
        ,1.0000,1.0000,1.0000,1.0000,-1.0000,1.0000,1.0000,1.0000
        ,1.0000,-1.0000,-1.0000,1.0000,-1.0000,1.0000]

x1 = normalize(x1)
x2 = normalize(x2)
x3 = normalize(x3)

w = []

print("Informe os parâmetros livres (vetor w): ")
w.append(float(input("Limiar inicial: ")))
w.append(float(input("Peso w1 inicial: ")))
w.append(float(input("Peso w2 inicial: ")))
w.append(float(input("Peso w3 inicial: ")))

print(w)
tx_aprendizado = 0.01

epocas = 0
erro = True

while(erro):
    erro = False
    for i in range(0, qtd_amostras):
        x = [-1, x1[i], x2[i], x3[i]]
        
        u = potencial(x[1], x[2], x[3], w)
        y = g(u)
        
        if y != d[i]:
            recalibrar(w, tx_aprendizado, d[i] - y, x)
            erro = True
    epocas += 1

print("\nRede Perceptron treinada")
print("\nParâmetros livres finais: " + str(w))
print("Epocas: " + str(epocas))


