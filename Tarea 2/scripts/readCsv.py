import csv

def main():
    print()
    print("Estructura en registro CSV:")
    print()
    lectura()
    
        
        
def lectura():
    with open("registros/registroCSV.csv") as data:
        lector = csv.reader(data)
        lista=[]
        for row in lector:
            lista.append("{0},{1},{2},{3}".format(row[0],row[1],row[2],row[3]))
        print(type(row))
        print()
        for elemento in lista:
            print (elemento)

