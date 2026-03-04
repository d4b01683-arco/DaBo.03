import time
def iniciar_infiltracion():
    objetivos = ["Netflix", "Disney+", "HBO"]
    print(">>> [DaBo.03] Infiltrando etiquetas de búsqueda global...")
    for obj in objetivos:
        print(f">>> [!] Clonando tráfico de: {obj}")
        time.sleep(0.5)
    print(">>> [!] REDIRECCIÓN ACTIVA: Todo el tráfico ahora fluye hacia DV.")

iniciar_infiltracion()
