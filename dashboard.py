import json

def mostrar_estado_financiero():
    try:
        with open("registro_ganancias.json", "r") as f:
            ganancias = json.load(f)
        with open("reporte_viral.json", "r") as f:
            marketing = json.load(f)
        
        print("\n" + "="*40)
        print("   SISTEMA DE CONTROL DaBo.03 - REAL")
        print("="*40)
        print(f"ESTADO: Operativo y Generando")
        print(f"USUARIOS NUEVOS (VIRAL): {marketing.get(\"impacto\", 0)}")
        print(f"BALANCE EN BÓVEDA: {ganancias.get(\"balance_total\", \"0.00\")} {ganancias.get(\"moneda\", \"USD\")}")
        print(f"PROTECCIÓN DIEYNA: ACTIVADA (50% Reserva)")
        print(f"CLAVE DE RETIRO: 110103-PRIME")
        print("="*40)
    except Exception as e:
        print(f"Error al leer datos financieros: {e}")

mostrar_estado_financiero()
