from xml.dom import minidom

def main():
    
    print()
    print("Estructura en registro XML:")
    print()
    impresion(readXml())
    
     
    
def readXml():
    data = minidom.parse("registros/registroXML.xml")
    equipos = data.getElementsByTagName("laptop")
    print(type(equipos))
    print()
    return equipos
def impresion(equipos):
    for equipo in equipos:    
        registro = equipo.getElementsByTagName("reg")[0]
        nombre = equipo.getElementsByTagName("nombre")[0]
        hz = equipo.getElementsByTagName("hz")[0]
        gamming = equipo.getElementsByTagName("gamming")[0]
        print("registro:%s " % registro.firstChild.data)
        print("nombre:%s" % nombre.firstChild.data)
        print("Hz:%s" % hz.firstChild.data)
        print("gamming:%s" % gamming.firstChild.data)
        print()
