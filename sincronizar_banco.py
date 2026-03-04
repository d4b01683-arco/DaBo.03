import json

def sincronizar_boveda():
    try:
        with open("boveda_cobro.json", "r") as f:
            datos = json.load(f)
        
        # Validacion del Pilar 4 (Seguridad)
        if datos["token_verificacion"] == "110103-Prime":
            print(">>> [DaBo.03] Validacion Exitosa.")
            print(f">>> Destino de fondos configurado: {datos[\"metodo_principal\"]}")
            print(">>> Microservicios autorizados para depositar ganancias.")
        else:
            print(">>> [ERROR] Clave de acceso denegada.")
    except Exception as e:
        print(f"Error en sincronizacion: {e}")

sincronizar_boveda()
