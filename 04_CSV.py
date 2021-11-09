#Wir erstellen eine CSV-Datei
import csv

#Datei anlegen
file1 = open("iris.csv","r")

#CSV Handler anlegen
reader = csv.reader(file1,delimiter=",")

for row in reader:
   # i = row[0]
    if float(row[0]) >= 5:
        print(row)

file1.close()

