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

normalized_mat = []

for i in range(len(table)):
    normalized_mat.append([])
    desv = np.std(table[i])
    med = np.average(table[i])
    for j in range(len(table)):
        normalized_mat[i].append( round((table[i][j] - med)/desv, 8 ))

for i in normalized_mat:
    print(i)

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('Matriz_Normalizada')
for i in range(len(normalized_mat)):
    for j in range(len(normalized_mat[i])):
        worksheet.write(i, j, label=normalized_mat[i][j])

workbook.save('Matriz_Normalizada.xls')