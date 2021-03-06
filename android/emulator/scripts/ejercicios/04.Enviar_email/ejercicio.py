# -*- coding: utf-8 -*-



import android
import time
import urllib2
import sys

droid = android.Android()

def enviar_mensaje(numero):
    try: 
        msg = "GPS" 
	asunto = u"Respuesta a la petición de localización GPS desde el numero %s" % (numero)
	para = "rengar666@gmail.com"
        droid.sendEmail(para, asunto, msg)
	droid.makeToast(u"Enviada respuesta")
    except:
        droid.makeToast("Error: " + str(sys.exc_info()[0]))


def servicio():
    
    while True:
        time.sleep(10)
	# Escuchar los mensajes SMS
        msg_solicitud = droid.smsGetMessages(True)
        
        for i in msg_solicitud.result:
            
            msg_sms = i["body"].strip().upper()
            if msg_sms == "GPS":
                droid.makeToast(u"Solicitud de localización recibida")
                droid.smsMarkMessageRead([i["_id"]], True)
                telefono = i["address"]
                enviar_mensaje(telefono)
		droid.makeToast(u"%s: %s" % (telefono,msg_sms))
                
                
                
    
if __name__ == "__main__":
    servicio()
