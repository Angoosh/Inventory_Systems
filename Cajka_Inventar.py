# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

line = []

with open("Cajovna.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line.append(row)
    print(line)
    print(line[2][0])




with open("Cajovna.csv", "w", newline='') as file:
    fileWrite = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    fileWrite.writerow(["Polozka","Pocet","Cena"])
    fileWrite.writerow(["Masala_Chai","250g",268])
    fileWrite.writerow(["Vanilla","100g",168])