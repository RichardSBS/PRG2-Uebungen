#Wir erstellen eine CSV-Datei
import csv

#Datei anlegen
file1 = open("daten1.csv","w")

#CSV Handler anlegen
writer = csv.writer(file1,delimiter=";")

writer.writerow(["ID","vorname","nachname"])
writer.writerow([1,"Max","Iliam"])
writer.writerow([2,"Hans","Wurst"])
liste10=[4,"HALLO","JAJA",5]
writer.writerow(liste10)
file1.close()
