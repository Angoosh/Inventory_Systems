import csv

FILE = "Cajovna"


def Open(file):
    line = []
    with open(file+".csv") as file:
        csv_reader = csv.reader(file, delimiter=',')
        #line_count = 0
        for row in csv_reader:
            line.append(row)
            print(line)
            print("Header:")
            print(line[0][0]+" "+line[0][1]+" "+line[0][2])
            print("\n")
    
    return line
    
def Edit():
    for i in range(len(line)):
        if i == 0:
            pass
        else:
            print(line[i][0]+": "+line[i][1])
            x = input("New value: ")
            if x == "":
                pass
            else:
                line[i][1] = x

    for i in range(len(line)):
        print(line[i])

def Write(file):
    with open(file+".csv", "w", newline='') as file:
        fileWrite = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        for i in range(len(line)):
            fileWrite.writerow(line[i])
            
def Append(file):
    with open(file+".csv", "a", newline='') as file:
        fileWrite = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        item = input("Polozka: ")
        qty = input("Mnozstvi: ")
        price = input("Cena: ")
        
        add = [item, qty, price]
        
        fileWrite.writerow(add)
       
def Default(file): 
    with open(file+".csv", "w", newline='') as file:
        fileWrite = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        fileWrite.writerow(["Polozka","Pocet","Cena"])
        fileWrite.writerow(["Masala_Chai","250g",268])
        fileWrite.writerow(["Vanilla","100g",168])
        

if __name__ == "__main__":
    """
    Default(FILE)
    """
    a = input("Edit [E] or Append [A]? ")
    if a == "E" or a == "e":
        line = Open(FILE)
        Edit()
        Write(FILE)
    elif a == "A" or a == "a":
        Append(FILE)
    else:
        print("Invalid option!\n")
    
