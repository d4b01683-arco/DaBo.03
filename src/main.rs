use std::fs;
use std::process::Command;

fn main() {
    println!("--- DaBo.03: Sistema de Ejecución Universal Activo ---");

    // 1. DaBo.03 busca tus órdenes en un archivo llamado 'orden.txt'
    let orden = fs::read_to_string("orden.txt").unwrap_or_else(|_| "Esperando orden...".to_string());
    println!("Orden recibida: {}", orden);

    // 2. Aquí DaBo.03 decide qué lenguaje usar. 
    // Por ahora, vamos a hacer que cree un script de Python para demostrar su poder.
    let codigo_ia = "print('DaBo.03 ha procesado tu orden y este es el resultado funcional.')";
    
    fs::write("ejecucion_dabo.py", codigo_ia).expect("Error al materializar");

    // 3. DaBo.03 ejecuta el código por sí mismo
    let salida = Command::new("python3")
        .arg("ejecucion_dabo.py")
        .output()
        .expect("Error en ejecución");

    println!("Resultado final:\n{}", String::from_utf8_lossy(&salida.stdout));
}
