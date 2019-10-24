import xlwt

def media(V, a, b):
    cont = 0
    media_a = 0
    media_b = 0

    for i in range(len(V)):
        if V[i][a] and V[i][b]:
            cont += 1
            media_a += V[i][a]
            media_b += V[i][b]

    media_a = media_a/cont
    media_b = media_b/cont

    return [media_a, media_b]

V = [
[29,	15.6,	647,	0.1742,	0.2820,	0.2180,	0.1571 ],
[29,	91.1,	917,	0.3744,	0.3834,	0.3128, False  ],
[29,	12.1,	460,	0.1181,	0.1180,	0.1507,	0.1163 ],
[29,	10.8,	709,	0.1714,	False,	0.2134,	0.1685 ],
[29,	18.4,	545,	0.1397,	False,	0.1981,	0.1357 ],
[29,	23.0,	541,	0.2736,	False,	0.2153,	0.1368 ],
[29,	11.7,	737,	0.1397,	False,	0.2253,	0.1760 ],
[29,	50.0,	930,	0.3110,	False,	0.3970,	False  ],
[29,	12.4,	697,	0.1944,	0.2148,	0.2176,	0.1667 ],
[29,	60.3,	898,	0.3211,	0.3507,	0.3609,	False  ],
[29,	11.1,	689,	0.1973,	False,	0.2093,	0.1640 ],
[29,	57.6,	914,	0.3729,	False,	0.3730,	False  ],
[29,	9.8,	395,	0.1109,	False,	0.1270,	0.1037 ],
[29,	13.3,	363,	0.1051,	False,	0.1269,	0.0988 ],
[29,	11.7,	436,	0.1195,	False,	0.1430,	0.1117 ],
[29,	80.2,	649,	0.2722,	False,	0.2406,	False  ],
[29,	13.0,	396,	0.1109,	False,	0.1355,	0.1047 ],
[0,	    0,	    294,	0.0731,	False,	0.0828,	0.0841 ],
[20,	0,	    294,	0.0778,	False,	0.0828,	0.0841 ],
[40,	0,	    294,	0.0824,	0.0680,	0.0828,	0.0841 ],
[60,	0,	    294,	0.0882, False,	0.0828,	0.0841 ],
[25,	50.0,	420,	0.1219,	False,	0.2184,	False  ],
[25,	70.0,	500,	0.1567,	False,	0.2554,	False  ],
[0,	    0,	    622,	0.1091,	0.1025,	0.1484,	0.1422 ],
[20,	0,	    622,	0.1149,	False,	0.1484,	0.1422 ],
[40,	0,	    622,	0.1219,	False,	0.1484,	0.1422 ],
[60,	0,	    622,	0.1283,	False,	0.1484,	0.1422 ],
[25,	50.0,	800,	0.2032,	0.1896,	0.3942,	False  ],
[25,	70.0,	920,	0.2554,	False,	0.4498,	False  ],
[21,	0,	    680,	0.2140,	False,	0.1600,	0.1542 ],
[21,	0,	    473,	0.1960,	False,	0.1186,	0.1140 ],
[21,	0,	    443,	0.1770,	0.1473,	0.1126,	0.1087 ],
[100,	0,	    680,	0.2500,	False,	0.1600,	0.1542 ],
[100,	0,	    473,	0.2440,	0.1979,	0.1186,	0.1140 ],
[100,	0,	    443,	0.2070,	False,	0.1126,	0.1087 ]
]

n = 3
m = 4
P = len(V)

matriz_correlacao = []

for i in range(n + m):
    matriz_correlacao.append([])
    for j in range(n + m):
        a = 0
        b = 0
        c = 0
        md = media(V, i, j)
        for l in range(P):
            d1 = V[l][i] - md[0]
            d2 = V[l][j] - md[1]
            a += d1*d2
            b += d1*d1
            c += d2*d2

        matriz_correlacao[i].append(round(a/((b*c)**0.5), 6))

print(matriz_correlacao)

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('Matriz_correlacao')
for i in range(len(matriz_correlacao)):
    for j in range(len(matriz_correlacao[i])):
        worksheet.write(i, j, label=matriz_correlacao[i][j])

workbook.save('Matriz_Correlacao.xls')