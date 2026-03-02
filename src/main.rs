use std::fs;
use std::process::Command;

fn main() {
    println!("--- DaBo.03: Iniciando Motor de Escritura ---");

    // Ejemplo: DaBo.03 decide escribir un script en Python solo
    let codigo_generado = "print('DaBo.03 ha tomado el control de este script de Python')";
    
    fs::write("generado.py", codigo_generado).expect("Error al escribir");
    println!("Documento escrito con éxito.");

    // DaBo.03 lo ejecuta para verificar que funciona
    let output = Command::new("python3")
        .arg("generado.py")
        .output()
        .expect("Error al ejecutar");

    println!("Resultado de la ejecución: {}", String::from_utf8_lossy(&output.stdout));
}
