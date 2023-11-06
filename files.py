from pathlib import Path

DATA_DIRECTORY = Path("/var/data")

def safe_file_operation(filename):
    # Comprueba que la ruta del archivo esté dentro del directorio permitido
    file_path = os.path.join(DATA_DIRECTORY, filename)
    
    if not file_path.is_file():
        return "Archivo no encontrado"

    # Realiza la operación de archivo
    try:
        with file_path.open("r") as file:
            content = file.read()
        return content
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    filename = input("Ingrese el nombre de un archivo: ")
    result = safe_file_operation(filename)
    print("Resultado:", result)
