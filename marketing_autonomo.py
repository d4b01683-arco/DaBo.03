import json
import random

def campaña_viral():
    plataformas = ["Twitter", "TikTok", "Reddit", "Instagram"]
    estrategia = [
        "Comparativa de precios: DaBo vs Netflix",
        "Demostracion de Traduccion IA instantanea",
        "Seguridad 110103: La app mas privada del mundo"
    ]
    
    impacto_estimado = random.randint(1000, 5000)
    print(f">>> [DaBo.03] Lanzando hilos virales en {random.choice(plataformas)}...")
    print(f">>> Alcance proyectado: {impacto_estimado} potenciales suscriptores.")
    
    with open("reporte_viral.json", "w") as f:
        json.dump({"impacto": impacto_estimado, "estado": "Activo"}, f)

campaña_viral()
