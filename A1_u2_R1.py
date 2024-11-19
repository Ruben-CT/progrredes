from flask import Flask, jsonify, request

app = Flask(__name__)

listaMascotas = {}

listaMascotas['Spaik'] = {
    "nombre": "Spaik",
    "edad": "20 meses",
    "raza": "Pitbull",
    "alergias": "Ninguna",
    "genero": "Macho",
    "observaciones": "cafe"
}

@app.route('/mascotas', methods=['GET'])
def obtener_mascotas():
    return jsonify(listaMascotas), 200

@app.route('/mascotas/buscar', methods=['GET'])
def buscar_mascota():
    nombre = request.args.get('nombre')
    raza = request.args.get('raza')

    for mascota in listaMascotas.values():
        if mascota['nombre'] == nombre or mascota['raza'] == raza:
            return jsonify(mascota), 200

    return jsonify({"mensaje": "Mascota no encontrada"}), 404

@app.route('/mascotas', methods=['POST'])
def agregar_mascota():
    datos = request.get_json()

    if not datos or 'nombre' not in datos or 'edad' not in datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    if datos['nombre'] in listaMascotas:
        return jsonify({"mensaje": "La mascota ya existe"}), 400

    listaMascotas[datos['nombre']] = datos
    return jsonify(datos), 201

@app.route('/mascotas/<string:nombre>', methods=['PUT'])
def modificar_mascota(nombre):
    if nombre not in listaMascotas:
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    datos = request.get_json()

    if not datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    nuevo_nombre = datos.get('nombre', nombre)
    if nuevo_nombre != nombre and nuevo_nombre in listaMascotas:
        return jsonify({"mensaje": "Ya existe una mascota con ese nombre"}), 400

    for key, value in datos.items():
        listaMascotas[nombre][key] = value

    if nuevo_nombre != nombre:
        listaMascotas[nuevo_nombre] = listaMascotas.pop(nombre)

    return jsonify(listaMascotas[nuevo_nombre]), 201

@app.route('/mascotas/<string:nombre>', methods=['DELETE'])
def eliminar_mascota(nombre):
    if nombre not in listaMascotas:
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    del listaMascotas[nombre]
    return jsonify({"mensaje": f"Mascota {nombre} eliminada correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)