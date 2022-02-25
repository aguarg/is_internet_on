"""
HACER/ IDEAS:
- el script debe correr y chequear cada 10 segundos si volvió internet haciendo un ping a Google
- Si hay conexión, mostrar el alerta, hacer el sonido y terminar con un mensaje en la consola?. 


- hacer ping a google
- si es true, llamar la función notificar y terminar el script 
- si es false, esperar 10 segundos y volver a verificar

- opciones?: 1- terminar script; 2- chequear sonido de alerta
"""


# Modules used:
import notify2
from playsound import playsound
import time
from ping3 import ping



# ================= FUNCTIONS: ======================== 
# Function that sends the alert:
def notificar():
    # Desktop notification:
    notify2.init('app name')

    mensaje = notify2.Notification("Conexión establecida",
                         "Que tengas buen día!",
                         "notification-message-im"
                        )
    mensaje.show()


  
    # Sound playing:
    playsound('alarma.wav')

    


# Function that checks for internet connection:
def buscando_conexion(sitio): 
    print("===========================")
    print("Chequeando conectividad...")   
    print("===========================")

    respuesta = ping(sitio)

    if respuesta == False:
        time.sleep(10)
        buscando_conexion(sitio)
        
    else:
        notificar()
        print("Conexión disponible! Que tengas un buen día.")
        


buscando_conexion("www.google.com")


