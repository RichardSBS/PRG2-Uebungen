#Wir erstellen eine CSV-Datei
import csv

#Datei anlegen
file1 = open("daten1.csv","a")

#CSV Handler anlegen
writer = csv.writer(file1,delimiter=";")

writer.writerow([9,"Fritz","lustig"])

file1.close()

