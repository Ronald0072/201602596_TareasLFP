import os

class registro():
    def __init__(self,num,nombre,edad,activo,saldo):
        self.name=nombre
        self.age=edad
        self.active=activo
        self.balance=saldo
        self.number=num

    def fila_html(self):
        fila="<tr><th scope=\"row\">"+self.number+"</th><td>"+self.name+"</td><td>"+self.age+"</td><td>"+self.active+"</td><td>"+self.balance+"</td></tr>"
        return fila


lista_registro=[]
def quemado():
    lista_registro.append(registro("1","Juan","12","True","123456"))
    lista_registro.append(registro("2","Pedro","22","False","654321"))
    lista_registro.append(registro("3","Ana","34","True","987654"))
    lista_registro.append(registro("4","Johny","45","True","654987"))
    lista_registro.append(registro("5","Jenny","28","False","321987"))
    lista_registro.append(registro("6","José","66","False","654123"))
    lista_registro.append(registro("7","Juan","12","True","123456"))
    lista_registro.append(registro("8","Pedro","22","False","654321"))
    lista_registro.append(registro("9","Ana","34","True","987654"))
    lista_registro.append(registro("11","Johny","45","True","654987"))
    lista_registro.append(registro("12","Jenny","28","False","321987"))
    lista_registro.append(registro("13","José","66","False","654123"))

def html(tablas):
    ht="""<!doctype html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

            <title>Registros</title>
        </head>
        <body>
            <section class="jumbotron text-center">
                <div class="container">
                    <h1 class="jumbotron-heading">Registros</h1>
                    <p class="lead text-muted">Bienvenido a los registros encontrados</p>
                </div>
            </section>
            <table class="table table-striped table-dark">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">NOMBRE</th>
                <th scope="col">EDAD</th>
                <th scope="col">ACTIVO</th>
                <th scope="col">SALDO</th>
                </tr>
            </thead>
            <tbody>"""+tablas+"""

            </tbody>
            </table>

            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        </body>
        </html>
        """
    return ht

def crear_html(texto):
    file = open("registros.html", "w")
    file.write(texto)
    file.close()
    os.system("registros.html")
    

def main():
    quemado()
    t=""
    for tab in lista_registro:
        t=t+tab.fila_html()
        t=t+"\n"
    crear_html(html(t))

    


main()
