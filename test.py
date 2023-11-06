import sqlite3

def buscar_usuario(usuario):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()

    # Utilizar una consulta parametrizada
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (usuario,))
    resultado = cursor.fetchall()

    conn.close()

    return resultado

nombre = input("Ingrese el nombre del usuario a buscar: ")
usuarios_encontrados = buscar_usuario(nombre)

if usuarios_encontrados:
    print("Usuario encontrado:", usuarios_encontrados)
else:
    print("Usuario no encontrado.")
