from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name)

# Conéctate a tu base de datos de MongoDB en Atlas
client = MongoClient("mongodb+srv://test11111111111111111155:test111111312412551@cluster.mongodb.net/test?retryWrites=true&w=majority")
db = client['frutas_db']
frutas_collection = db['frutas']

# Método GET para obtener la lista de frutas desde la base de datos
@app.route('/frutas', methods=['GET'])
def get_frutas():
    frutas = list(frutas_collection.find({}, {'_id': 0}))  # Recupera todas las frutas sin el campo "_id"
    return jsonify(frutas)

# Método POST para agregar una fruta a la base de datos
@app.route('/frutas', methods=['POST'])
def add_fruta():
    data = request.get_json()
    fruta_nombre = data.get('nombre')
    if fruta_nombre:
        frutas_collection.insert_one({'nombre': fruta_nombre})
        return 'Fruta agregada', 201
    else:
        return 'Falta el nombre de la fruta', 400

# Método DELETE para eliminar una fruta por nombre de la base de datos
@app.route('/frutas/<nombre>', methods=['DELETE'])
def delete_fruta(nombre):
    result = frutas_collection.delete_one({'nombre': nombre})
    if result.deleted_count > 0:
        return 'Fruta eliminada', 200
    else:
        return 'Fruta no encontrada', 404

if __name__ == '__main__':
    app.run(debug=True)

