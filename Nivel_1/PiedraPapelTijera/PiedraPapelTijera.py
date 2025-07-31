import tkinter as tk
import random
from tkinter import messagebox


eleccion_jugador = ""
eleccion_bot = ""
resultados = [" 🪨 Piedra", " 📄 Papel", " ✂️ Tijera"]

puntos_jugador = 0
puntos_bot = 0

def toca_Piedra():
    global eleccion_jugador
    global eleccion_bot
    global puntos_jugador
    global puntos_bot

    eleccion_jugador = " 🪨 Piedra"
    eleccion_bot = random.choice(resultados)

    if eleccion_bot == " 🪨 Piedra":
        texto = "¡Ha habido un empate!"
    elif eleccion_bot == " 📄 Papel":
        texto = "Boti boti ha ganado esta ronda."
        puntos_bot+=1
    else:
        texto = "¡Has ganado la ronda!"
        puntos_jugador+=1

    resultado.config(text=f"Resultado:\n\nElegiste:{eleccion_jugador}\n\nBoti boti eligio:{eleccion_bot}\n\n{texto}")

    if puntos_jugador > puntos_bot:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n 🏆 Vas ganando")
    elif puntos_bot > puntos_jugador:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n 😈 Boti boti domina")
    else:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n Empate")

    if puntos_jugador == 5:
        messagebox.showinfo(
        f"¡Has ganado!", "ENHORABUENA"
    )
        reiniciar_marcador()
    elif puntos_bot == 5:
        messagebox.showinfo(
        f"Boti boti te a destrozado!","Perdedor"
    )
        reiniciar_marcador()


def toca_Papel():
    global eleccion_jugador
    global eleccion_bot
    global puntos_jugador
    global puntos_bot
    
    eleccion_jugador = " 📄 Papel"
    eleccion_bot = random.choice(resultados)

    if eleccion_bot == " 📄 Papel":
        texto = "¡Ha habido un empate!"
    elif eleccion_bot == " ✂️ Tijera":
        texto = "Boti boti ha ganado esta ronda."
        puntos_bot+=1
    else:
        texto = "¡Has ganado la ronda!"
        puntos_jugador+=1

    resultado.config(text=f"Resultado:\n\nElegiste:{eleccion_jugador}\n\nBoti boti eligio:{eleccion_bot}\n\n{texto}")
    
    if puntos_jugador > puntos_bot:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n 🏆 Vas ganando")
    elif puntos_bot > puntos_jugador:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n 😈 Boti boti domina")
    else:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n Empate")    

    if puntos_jugador == 5:
        messagebox.showinfo(
        f"¡Has ganado!","ENHORABUENA"
        )
        reiniciar_marcador()
    elif puntos_bot == 5:
        messagebox.showinfo(
        f"Boti boti te a destrozado!","Perdedor"
    )
        reiniciar_marcador()


def toca_Tijera():
    global eleccion_jugador
    global eleccion_bot
    global puntos_jugador
    global puntos_bot
    
    eleccion_jugador = " ✂️ Tijera"
    eleccion_bot = random.choice(resultados)

    if eleccion_bot == " ✂️ Tijera":
        texto = "¡Ha habido un empate!"
    elif eleccion_bot == " 🪨 Piedra":
        texto = "Boti boti ha ganado esta ronda."
        puntos_bot+=1
    else:
        texto = "¡Has ganado la ronda!"
        puntos_jugador+=1

    resultado.config(text=f"Resultado:\n\nElegiste:{eleccion_jugador}\n\nBoti boti eligio:{eleccion_bot}\n\n{texto}")

    if puntos_jugador > puntos_bot:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n 🏆 Vas ganando")
    elif puntos_bot > puntos_jugador:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n 😈 Boti boti domina")
    else:
        marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}\n\n Empate")

    if puntos_jugador == 5:
        messagebox.showinfo(
        f"¡Has ganado!","ENHORABUENA"
    )
        reiniciar_marcador()
    elif puntos_bot == 5:
        messagebox.showinfo(
        f"Boti boti te a destrozado!","Perdedor"
    )
        reiniciar_marcador()

def reiniciar_marcador():
    global puntos_bot
    global puntos_jugador

    puntos_bot = 0
    puntos_jugador = 0

    marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}")

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("500x480")

marcador = tk.Label(ventana, text="Marcador: ")
marcador.pack(pady=10)

piedra = tk.Button(ventana, text="🪨 Piedra", width=20, command=toca_Piedra)
piedra.pack(pady=10)

papel = tk.Button(ventana, text="📄 Papel", width=20, command=toca_Papel)
papel.pack(pady=10)

tijera = tk.Button(ventana, text="✂️ Tijeras", width=20, command=toca_Tijera)
tijera.pack(pady=10)

resultado = tk.Label(ventana, text=f"Resultado:\n\nElegiste: {eleccion_jugador}")
resultado.pack(pady=10)

reseteo = tk.Button(ventana, text="Reiniciar Marcador", command=reiniciar_marcador)
reseteo.pack(pady=10)

if puntos_jugador == 5:
    messagebox.showinfo(
        f"¡Has ganado!\n\nENHORABUENA"
    )
elif puntos_bot == 5:
    messagebox.showinfo(
        f"Boti boti te a destrozado!\n\nPerdedor"
    )

ventana.mainloop()