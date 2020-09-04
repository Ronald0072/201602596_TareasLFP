ent1="__servidor1"
ent2="3servidor"


def lector(entrada): 
    entrada_list=list(entrada)
    estado=0
    cont=0
    for caracter in entrada_list:
        codigo=ord(caracter)
        if estado==0:
            if codigo==95:
                estado=1
                cont=cont+1
            else:
                if (codigo>=97 and codigo<=122)or(codigo>=65 and codigo<=90):
                    estado=2
                    cont=cont+1
                else:
                    error(entrada,cont)
                    break
        else:
            if estado==1:
                if codigo==95:
                    estado=1
                    cont=cont+1
                else:
                    if (codigo>=97 and codigo<=122)or(codigo>=65 and codigo<=90):
                        estado=3
                        cont=cont+1
                    else:
                        error(entrada,cont)
                        break
            else:
                if estado==2:
                    if (codigo>=97 and codigo<=122)or(codigo>=65 and codigo<=90):
                        estado=2
                        cont=cont+1
                    else:
                        if codigo>=48 and codigo<=57:
                            estado=4
                            cont=cont+1
                        else:
                            error(entrada,cont)
                            break
                else:
                    if estado==3:
                        if (codigo>=97 and codigo<=122)or(codigo>=65 and codigo<=90):
                            estado=3
                            cont=cont+1
                        else:
                            if codigo>=48 and codigo<=57:
                                estado=4
                            else:
                                error(entrada,cont)
                                break
                    else:
                        if estado==4:
                            if caracter!="\n":
                                error(entrada,cont)
                                break
                        
    if estado==4:
        print("\nAnálisis finalizado con éxito")
        print(entrada+" no tiene errores lexicos")
        print("\n ------------------------------------ ")


def error(entrada,col):
    print("\nAnalisis Finalizado, sin exito")
    print(entrada+" tiene errores lexicos en la columna "+str(col) )
    print("\n ------------------------------------ ")


def main():
    lector(ent1)
    lector(ent2)


    print("""Nota:
    Este automata fue corregido, en el foro de slak\n""")

main()

                    