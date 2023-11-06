from flask import Flask, request, jsonify

app = Flask(__name__)

frutas = []

# Método GET para obtener la lista de frutas
@app.route('/frutas', methods=['GET'])
def get_frutas():
    return jsonify(frutas)

# Método POST para agregar una fruta a la lista
@app.route('/frutas', methods=['POST'])
def add_fruta():
    data = request.get_json()
    fruta_nombre = data.get('nombre')
    if fruta_nombre:
        frutas.append(fruta_nombre)
        return 'Fruta agregada', 201
    else:
        return 'Falta el nombre de la fruta', 400

# Método DELETE para eliminar una fruta por nombre
@app.route('/frutas/<nombre>', methods=['DELETE'])
def delete_fruta(nombre):
    if nombre in frutas:
        frutas.remove(nombre)
        return 'Fruta eliminada', 200
    else:
        return 'Fruta no encontrada', 404

if __name__ == '__main__':
    app.run(debug=True)
