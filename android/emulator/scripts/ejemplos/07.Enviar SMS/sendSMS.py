# -*- coding: utf-8 -*-

#Importando el módulo android y el módulo time
import android

#Creando la instancia droid del objeto Android
droid = android.Android()

#Asignando el número de teléfono y mensaje
telefono ="034777777777"
mensaje = "Esta es una prueba de envio de sms a la hora %s" %time.ctime()

#Enviar mensaje a la pantalla de android con la info del número y mensaje
droid.makeToast("enviando mensaje a %s, con el siguiente contenido: %s" %(telefono,mensaje))

#Enviando el mensaje de texto
droid.smsSend(telefono,mensaje)
