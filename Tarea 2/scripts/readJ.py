import json

def readJson():
    file = open("registros/registroJSON.json")
    data = json.load(file)
    file.close()
    return data
def main():
    dict = readJson()
    print()
    print("Estructura en registro JSON:")
    print("                      Arreglo de objetos")
    print()

    for element in dict:
        print(str(element).replace("{","").replace("}","").replace("'",""))

