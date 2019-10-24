import numpy as np 
import xlrd, xlwt

arq = xlrd.open_workbook("table.xlsx")
plan = arq.sheets()[0]

table = []
for i in range(5, plan.nrows):
    table.append([])
    for j in range(2, len(plan.row_values(i))-1):
        value = plan.row_values(i)[j]
        if(value == "—" or value == ""):
            value = 0
        table[i-5].append(float(value))

table = np.asarray(table)
table = table.transpose()
table = table.tolist()

print(table)

matriz_cov = []

for i in range(len(table)):
    matriz_cov.append([])
    for j in range(len(table)):
        matriz_cov[i].append(np.cov(table[i], table[j])[0][1])


workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('Matriz_Covariancia')
for i in range(len(matriz_cov)):
    for j in range(len(matriz_cov[i])):
        worksheet.write(i, j, label=matriz_cov[i][j])

workbook.save('matriz covariancia.xls')