from decouple import config 

#LO DEFINIMOS EN settings.py/TEMPLATES
def get_enviroment_server(request):
    entorno = config('ENVIROMENT')
    
    if entorno == "TEST":
        entorno_color = "danger"
    elif entorno == "DEV":
        entorno_color = "danger"
    else:
        entorno_color = "success"

    return {
        "entorno" : entorno,
        "entorno_color" : entorno_color,
    }
