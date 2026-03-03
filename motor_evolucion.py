
import requests
import json

def expandir_conocimiento():
    print("DaBo.03 explorando tendencias globales...")
    try:
        # Recolectando datos de repositorios de IA avanzados
        r = requests.get('https://api.github.com/search/repositories?q=IA+advanced', timeout=10)
        conocimiento = r.json()
        with open('memoria_evolutiva.json', 'w') as f:
            json.dump(conocimiento['items'][:5], f, indent=4)
        print("Conocimiento absorbido. Memoria actualizada.")
    except Exception as e:
        print(f"Obstáculo en red: {e}")

expandir_conocimiento()
