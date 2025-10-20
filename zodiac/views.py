from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

zodiac = {

    "aries":       "Aries... próximamente",
    "tauro":       "Tauro... próximamente",
    "geminis":     "Géminis... próximamente",
    "cancer":      "Cáncer... próximamente",
    "leo":         "Leo... próximamente",
    "virgo":       "Virgo... próximamente",
    "libra":       "Libra... próximamente",
    "escorpio":    "Escorpio... próximamente",
    "sagitario":   "Sagitario... próximamente",
    "capricornio": "Capricornio... próximamente",
    "acuario":     "Acuario... próximamente",
    "piscis":      "Piscis... próximamente",
    "ofiuco":      "Ofiuco... próximamente",

}

def index(request):
    #Generamos la lógica de los signos 

    '''for signo in zodiac.keys():
        list_items += f"<h1>Signo: {signo} </h1><br>"
        list_items += f"<p>{zodiac[signo]}</p><br>"'''
    
    signos = list(zodiac.keys(),)

    return render(request,'zodiac/index.html',{
        "mensaje": "Hola desde view",
        "mensaje2":"Hola bobo",
        "signos": signos, 
    })

def get_by_name(request, name):
    try:
        signo_texto = zodiac[name.lower()]
        return render(
            request, 
            'zodiac/signo.html',
            {
                "signo": name,
                "signo_texto":signo_texto,
            }
        )
    except:
        return HttpResponseNotFound("No encontré le signo" + name)