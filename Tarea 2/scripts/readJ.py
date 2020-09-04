import json

data=None

def readJson():
    file = open("registros/registroJSON.json")
    data = json.load(file)
    print(type(data))
    print()
    file.close()    
    return data
def main():

    print()
    print("Estructura en registro JSON:")
    print()
    dict = readJson()
    for element in dict:
        el=str(element).replace("{","").replace("}","").replace("'","").replace(" ","")
        el=el.lower().replace("registro:","").replace("nombre:","").replace("hz:","").replace("gamming:","")
        dat=el.split(",")
        
            
        print("-------------")

        
        
    
main()
