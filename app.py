#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

opciones = ["piedra", "papel", "tijeras"]

while True:
    eleccion_jugador = input("Elige una opción: piedra, papel o tijeras: ").lower()
    if eleccion_jugador not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    eleccion_oponente = random.choice(opciones)
    if eleccion_jugador == eleccion_oponente:
        print("Es un empate.")
    elif (eleccion_jugador == "piedra" and eleccion_oponente == "tijeras") or \
         (eleccion_jugador == "tijeras" and eleccion_oponente == "papel") or \
         (eleccion_jugador == "papel" and eleccion_oponente == "piedra"):
        print("Has ganado.")
    else:
        print("Has perdido.")
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        break