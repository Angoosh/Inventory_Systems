import csv

FILE = "Cajovna"


def Open(file):
    line = []
    with open(file+".csv") as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            line.append(row)
    
    return line
    
def List(file):
    line = []
    with open(file+".csv") as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            line.append(row)

        print("\n")
        for i in range(len(line)):
            print(line[i])

def Edit():
    for i in range(len(line)):
        if i == 0:
            pass
        else:
            print(line[i][1]+": "+line[i][2])
            x = input("New value: ")
            if x == "":
                pass
            else:
                line[i][2] = x

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
        ID = "ID"+str(len(line)-1)
        
        add = [ID, item, qty, price]
        
        fileWrite.writerow(add)
        
def Search():
    search = "ID"+input("Item: ")
    for i in range(len(line)):
        try:
            line[i].index(search)
            print(line[i])
            return i
        except:
            pass
 
def Edit_Adv():
    s = Search()
    print(line[s][1]+": "+line[s][2])
    x = input("New value: ")
    if x == "":
        pass
    else:
        line[s][2] = x
    
       
def Default(file): 
    with open(file+".csv", "w", newline='') as file:
        fileWrite = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        fileWrite.writerow(["ID", "Polozka","Mnozstvi","Cena"])
        fileWrite.writerow(["ID0", "Masala_Chai",250 ,268])
        fileWrite.writerow(["ID1", "Vanilla",100 ,168])
        

if __name__ == "__main__":

    while True:
        a = input("Edit [E], Append [A], List[L], Search[S] or Exit [Exit]? ")
        if a == "E" or a == "e":
            line = Open(FILE)
            Edit_Adv()
            Write(FILE)
        elif a == "A" or a == "a":
            while True:
                line = Open(FILE)
                Append(FILE)
                a = input("Next item? [Y/n] ")
                if a == "Y" or a == "y":
                    pass
                else:
                    break
        elif a == "L" or a == "l":
            line = List(FILE)
        elif a == "Exit" or a == "exit":
            break
        elif a == "S" or a == "s":
            line = Open(FILE)
            Search()
        elif a == "B" or a == "b":
            line = Open(FILE)
            Edit()
            Write(FILE)
        elif a == "Default":
            x = input("Really? [Y/n] ")
            if x == "Y" or x == "y":
                Default(FILE)
            else:
                pass
        else:
            print("Invalid option!\n")
