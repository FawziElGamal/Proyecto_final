from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola Django")

def probando_template_2(request):
    
    notas = [4, 5, 6, 7, 8, 9]

    diccionario = {"nombre": "Rene", "apellido": "Roro", "ahora": str(datetime.now()), "notas": notas}

    mi_html = open('G:\Mi unidad\CoderHouse\Clase 15. Django I\proyecto\Tienda_de_repuestos\Tienda_de_repuestos\\templates\index.html')

    # plantilla = Template(mi_html.read())

    # mi_html.close()

    # contexto = Context(diccionario)

    # documento = plantilla.render(contexto)

    plantilla = loader.get_template('index.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)