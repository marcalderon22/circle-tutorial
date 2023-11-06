import os

def unsafe_file_operation(filename):
    # Este código concatena una entrada del usuario en una ruta de archivo sin validación.
    # Podría permitir a un atacante acceder a archivos no deseados en el sistema.
    file_path = "/var/data/" + filename
    with open(file_path, "r") as file:
        content = file.read()
    return content

if __name__ == "__main__":
    filename = input("Ingrese el nombre de un archivo: ")
    result = unsafe_file_operation(filename)
    print("Contenido del archivo:", result)
