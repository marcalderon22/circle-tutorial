import os

DATA_DIRECTORY = "/var/data/"

def safe_file_operation(filename):
    # Comprueba que la ruta del archivo esté dentro del directorio permitido
    file_path = os.path.abspath(os.path.join(DATA_DIRECTORY, filename))

    if not file_path.startswith(DATA_DIRECTORY):
        return "Ruta de archivo no permitida"
    
    # Realiza la operación de archivo
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Archivo no encontrado"
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    filename = input("Ingrese el nombre de un archivo: ")
    result = safe_file_operation(filename)
    print("Resultado:", result)
