from flask import Flask, jsonify, request
from logic import Tablero, Cuadro, Jugador

app = Flask(__name__)

# Inicialización del juego
tablero = Tablero(5)
jugador = Jugador("Jugador 1")
puntaje = 0
tiempo_restante = 60


@app.route("/api/tablero", methods=["GET"])
def obtener_tablero():
    """Devuelve el tablero con operaciones ocultas."""
    data = []
    for i in range(tablero.tamanio):
        fila = []
        for j in range(tablero.tamanio):
            fila.append({
                "i": i,
                "j": j,
                "pintado": tablero.get_cuadro(i, j).esta_pintado()
            })
        data.append(fila)
    return jsonify(data)


@app.route("/api/responder", methods=["POST"])
def responder():
    global puntaje
    data = request.get_json()
    i, j = data["i"], data["j"]
    respuesta_usuario = int(data["respuesta"])
    cuadro = tablero.get_cuadro(i, j)

    if cuadro.esta_pintado():
        return jsonify({"mensaje": "Ya respondido", "puntaje": puntaje})

    correcta = cuadro.comparar_respuesta(respuesta_usuario)
    cuadro.pintar()
    puntaje += 5 if correcta else -10

    return jsonify({
        "correcta": correcta,
        "puntaje": puntaje,
        "operacion": cuadro.operacion
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)