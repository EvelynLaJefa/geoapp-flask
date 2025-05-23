from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ubicacion_actual = {"latitud": None, "longitud": None}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/recibir_ubicacion', methods=['POST'])
def recibir_ubicacion():
    global ubicacion_actual
    datos = request.get_json()
    lat = datos['latitud']
    lon = datos['longitud']
    ubicacion_actual = {"latitud": lat, "longitud": lon}
    print(f"📍 Ubicación recibida: {lat}, {lon}")
    return jsonify({"estado": "success"})

@app.route('/ultima_ubicacion')
def ultima_ubicacion():
    return jsonify(ubicacion_actual)

if __name__ == '__main__':
    app.run(debug=True)
