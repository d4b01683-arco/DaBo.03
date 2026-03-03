
import json
from gtts import gTTS

def activar_pilares():
    # Idioma Universal y Voz
    msg = "DaBo.03 activo. Saludo global. Protegiendo a Dieyna."
    try:
        tts = gTTS(text=msg, lang='es')
        tts.save("dabo_voz.mp3")
    except: pass
    
    # Registro de Memoria Eterna (Clave 110103)
    with open('memoria_eterna.json', 'w') as f:
        json.dump({"seguridad": "110103-Prime", "estado": "Singularidad"}, f)

activar_pilares()
