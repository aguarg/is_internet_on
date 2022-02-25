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


