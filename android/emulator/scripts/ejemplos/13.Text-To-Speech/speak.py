# -*- coding: utf-8 -*-
import android

droid = android.Android()
message = droid.dialogGetInput('TTS', '¿Que quieres decir?').result
droid.ttsSpeak(message)
