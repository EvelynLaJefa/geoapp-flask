from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/recibir_ubicacion', methods=['POST'])
def recibir_ubicacion():
    datos = request.get_json()
    lat = datos['latitud']
    lon = datos['longitud']
    print(f"📍 Ubicación recibida: {lat}, {lon}")
    return jsonify({"estado": "success"})

if __name__ == '__main__':
    app.run(debug=True)

