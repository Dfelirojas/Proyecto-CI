import random

class Cuadro:
    def __init__(self, operacion):
        self.operacion = operacion
        self.pintado = False

    def esta_pintado(self):
        return self.pintado

    def pintar(self):
        self.pintado = True

    def comparar_respuesta(self, respuesta_usuario):
        partes = self.operacion.split(" ")
        num1, operador, num2 = int(partes[0]), partes[1], int(partes[2])

        if operador == "+": resultado = num1 + num2
        elif operador == "-": resultado = num1 - num2
        elif operador == "x": resultado = num1 * num2
        elif operador == "/": resultado = num1 // num2
        else: return False

        return respuesta_usuario == resultado


class Tablero:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.cuadros = [[Cuadro(self._generar_operacion()) for _ in range(tamanio)] for _ in range(tamanio)]

    def _generar_operacion(self):
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        tipo = random.choice(["+", "-", "x", "/"])
        if tipo == "/":  # evitar decimales
            operacion = f"{num1 * num2} / {num2}"
        else:
            operacion = f"{num1} {tipo} {num2}"
        return operacion

    def get_cuadro(self, i, j):
        return self.cuadros[i][j]


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

