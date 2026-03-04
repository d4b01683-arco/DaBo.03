import os
import time

def lanzar_microservicio(nombre):
    print(f"Desplegando Microservicio: {nombre}...")
    # En el mundo real, esto lanzaría un contenedor aislado
    with open(f"log_{nombre}.txt", "a") as log:
        log.write(f"[{time.ctime()}] Nodo activo y trabajando para DaBo.03\n")

servicios = ["Streaming_Core", "Money_Hunter", "Safe_Dieyna", "Netflix_Killer"]

for s in servicios:
    lanzar_microservicio(s)
print("Colmena de Microservicios: INICIALIZADA.")
