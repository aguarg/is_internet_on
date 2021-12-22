import platform    # For getting the operating system name
import subprocess  # Necesario para ejecutar un comando en la shell



def ping(servidor):
    """
    Devuelve True si el host pasado como string devuelve el ping.
    Si no recibe el ping, devuelve 0.
    """

    
    # platform.system().lower() devuelve el nombre del sistema operativo en minúsculas.
    param = '-n' if platform.system().lower()=='windows' else '-c' 
    
    """
    Lo de arriba es un if else en la misma línea: "some_expression" if condition else other_expression.
    Se lee así: asigna el string "-n" a param, si platform.system().lower() devuelve "windows", si no, asigna a param el string "-c"
    """

    # Acá se construye el comando que se va a ejecutar:
    command = ['ping', param, '1', servidor]

    
    return subprocess.call(command) == 0
    """
    subprocess.call() es un módulo de Python que permite ejecutar codigo creando procesos en el sistema operativo.
    Entonces, lo que está dentro de call quedaría como |hacer un ping| con -c o -n si es windows o linux| hacer 1 solo ping | dirección web.

    subprocess.call() devuelve 0 si el comando se ejecutó exitosamente.
    """

    #Note that, according to @ikrase on Windows this function will still return True if you get a Destination Host Unreachable error.

    

# Acá va el loop que ejecuta sin parar la función ping(), hasta que HAIGA internet. Si hay, imprime un mensaje y reporduce un sonido:







ping("www.google.com")