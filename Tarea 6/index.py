class analisis():

    def __init__(self):
        self.token=""
        self.lexema=""
    
    def valores(self,tok,lex):
        self.token=tok
        self.lexema=lex

#-------------------------------------------------#
    #      metodos y funciones    #
#-------------------------------------------------#

entrada="""
(
    <
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
        [_atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = false
    >,
    <
        [atributo_numerico] = -56.4,
        [atributo_cadena] = "este es otro ejemplo, las cadeas pueden ser muy largas",
        [atributo_booleano] = false
    >
)
"""

def automata():
    lista_entrada = list(entrada+" ")
    cont=0
    estado=0
    lexema=""
    signo="_positivo"
    terminado=False
    while cont<len(lista_entrada):
        carac=lista_entrada[cont]
        if estado==0:
            if caracter(carac)==5:          #salto de linea o espacio en blanco
                estado=0
                cont=cont+1

            elif caracter(carac)==4:        #Simbolo del lenguaje, lo envia al estado 8
                estado=8
            elif caracter(carac)==2 or caracter(carac)==7:      #Letra o guion bajo, envia al estado 1 (estado de aceptacion)
                lexema=lexema+str(carac)
                estado=1
                cont=cont+1
            elif caracter(carac)==3:            #Digito, lo envia al estado 2
                lexema=lexema+str(carac)
                estado=2
                cont=cont+1
            elif caracter(carac)==8:                #Signo + ó -, lo envia al estado 5
                lexema=lexema+str(carac)
                estado=5
                cont=cont+1
            elif caracter(carac)==1:                #Cadena de caracteres
                lexema=lexema+str(carac)
                estado=6
                cont=cont+1
            else:
                break


        elif estado==1:
            if caracter(carac)==2 or caracter(carac)==7:
                estado=1
                lexema=lexema+str(carac)
                cont=cont+1
            elif caracter(carac)==5 or caracter(carac)==4:
                tipo_palabra(lexema)
                lexema=""
                estado=0
            else:
                
                print("Error")
                
                break
        elif estado==2:
            if caracter(carac)==3:
                lexema=lexema+str(carac)
                estado=2
                cont=cont+1
            elif caracter(carac)==6:
                lexema=lexema+str(carac)
          
                estado=3
                cont=cont+1
            elif caracter(carac)==5 or caracter(carac)==4:
                print(lexema+" --- Tk_Numero"+signo)
                signo="_Positivo"
                lexema=""
                estado=0
            else:
                
                print("Error")
                
                break    
        elif estado==3:
            if caracter(carac)==3:
                lexema=lexema+str(carac)
                estado=4
                cont=cont+1
            else:
               
                print("Error")
                
                break    
                
        elif estado==4:
            if caracter(carac)==3:
                lexema=lexema+str(carac)
                estado=4
                cont=cont+1
            elif caracter(carac)==5 or caracter(carac)==4:
                print(lexema+" --- Tk_Numero_Decimal"+signo)
                lexema=""
                estado=0
            else:
                
                print("Error")
                
                break 
        elif estado==5:
            if str(carac)=="+":
                signo="_Positivo"
            else:
                signo="_Negativo"

            if caracter(carac)==3:
                estado=2
            else:
                
                print("Error")
                
                break 

        elif estado==6:
            if ord(carac)==10:
                print("Error")
                break
            elif caracter(carac)!=1:
                lexema=lexema+str(carac)
                estado=6
                cont=cont+1
            else:
                lexema=lexema+str(carac)
                estado=7
                cont=cont+1
                

        elif estado==7:
            if caracter(carac)==5 or caracter(carac)==4:
                print(lexema+" --- Tk_Cadena_de_Caracteres")
                estado=0
            else:
               
                print("Error")
                
                break 
        elif estado==8:
            lexema=carac
            simbolo(ord(carac),lexema)
            lexema=""
            estado=0
            cont=cont+1
        else:
            print("error")
            break

    if cont==len(lista_entrada):
        terminado=True

    return terminado

#verifica si es true o false, o si es una palabra cualquiera
def tipo_palabra(lexema):           
    if lexema=="true":
        print(lexema+" --- Tk_True")
    elif lexema=="false":
        print(lexema+" --- Tk_False")
    else:
        print(lexema+" --- Tk_Palabra")
#Elije cual es el simbolo asociado y le asigna su token

def simbolo(codigo,lexema):
    if codigo==40:
        print(lexema+" --- TK_Parentesis_Abierto")
    elif codigo==41:
        print(lexema+" --- TK_Parentesis_Cerrado")
    elif codigo==60:
        print(lexema+" --- TK_Menor_Que")
    elif codigo==62:
        print(lexema+" --- TK_Mayor_Que")
    elif codigo==91:
        print(lexema+" --- TK_Corchete_Abierto")
    elif codigo==93:
        print(lexema+" --- TK_Corchete_Cerrado")
    elif codigo==61:
        print(lexema+" --- TK_Signo_Igual")
    elif codigo==44:
        print(lexema+" --- TK_Coma")

#Retorna:
        #---1=comillas simples o dobles
        #---2=letra
        #---3=Digito
        #---4=simbolo [{(},{)},{<},{>}{[},{]},{=},{,}]
        #---5=delimitador [{espacio}{salto de linea}]
        #---6=punto
        #---7=guion bajo
        #---8=signo +,-
        #---9=cualquier otro caracter
def caracter(caracter):
    codigo=ord(caracter)
    if codigo==34 or codigo==39:
        return 1
    elif (codigo>=97 and codigo<=122)or(codigo>=65 and codigo<=90) or codigo==95:
        return 2
    elif codigo>=48 and codigo<=57:
        return 3
    elif codigo==40 or codigo==41 or codigo==60 or codigo==62 or codigo==91 or codigo==93 or codigo==61 or codigo==44:            
        return 4
    elif codigo==32 or codigo==10:
        return 5
    elif codigo==46:
        return 6
    elif codigo==95:
        return 7
    elif codigo==43 or codigo==45:
        return 8
    else:
        return 9
                    



def main():
    print("""



    Listado de Tokens obtenidos durante el analisis lexico de la entrada

    Nota: La impresión se realiza durante el análisisi léxico, por lo que si encuentra un error se detendrá el analisisi en ese momento

    presione enter para iniciar el analisis

    """)
    input()
    if automata()==True:
        print("""

        Examen completado con éxito

        No se encontró ningún error léxico durante el análisisi

        """)
    else:
        print("""

        Hubo un error en el analisisi lexico

        Verifique su entrada
        
        """)


main()
