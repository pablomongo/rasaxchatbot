import csv
archivo = []
f = open('/home/pablo/Escritorio/rasaprojects/actions/datos.csv')
csv_f = csv.reader(f)
for row in csv_f:
    archivo.append(row)
name = "Pablo"
archivo.append([name])
#print(last_row)
#last_row.append(', 5')
#archivo = archivo[:-1]
#archivo.append(last_row)
#print(archivo[-1])
print(archivo)
#archivo.append(["Pablo","25","Mujer","si"])
with open('/home/pablo/Escritorio/rasaprojects/actions/datos.csv','w', newline='\n') as file:
    writer = csv.writer(file)
    writer = csv.writer(file, delimiter=',')
    writer.writerows(archivo)


#csv_f = csv.reader(f)
#for row in csv_f:
#    print(row[2])
#workbook = openpyxl.load_workbook(filename='datos.xlsx')
#worksheet = workbook['Hoja1']
#nrows = len(worksheet['A'])
#worksheet.cell(row=nrows+1, column=1, value = 'Pablo')
#worksheet.cell(row=nrows+1, column=2, value = '25')
#worksheet.cell(row=nrows+1, column=3, value = 'No')
#workbook.save('datos.xlsx')

#print(nrows)
