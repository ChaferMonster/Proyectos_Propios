import tkinter as tk
import random
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

# 🎮 --- VARIABLES DEL JUEGO ---
eleccion_jugador = ""
eleccion_bot = ""
resultados = [" 🪨 Piedra", " 📄 Papel", " ✂️ Tijera"]
jugadas_jugador = {" 🪨 Piedra":0, " 📄 Papel":0, " ✂️ Tijera":0}
puntos_jugador = 0
puntos_bot = 0
ganar_a = {
    " 🪨 Piedra": " 📄 Papel",
    " 📄 Papel": " ✂️ Tijera",
    " ✂️ Tijera": " 🪨 Piedra"
}

# --- Lógica del juego ---
def jugar(eleccion):
    global eleccion_jugador, eleccion_bot, puntos_jugador, puntos_bot
    eleccion_jugador = eleccion
    jugadas_jugador[eleccion_jugador] +=1

    ganadores = {
    " 🪨 Piedra": " ✂️ Tijera",
    " 📄 Papel": " 🪨 Piedra",
    " ✂️ Tijera": " 📄 Papel"
    }

    # 🤖 --- LÓGICA DE LA IA ---
    if puntos_jugador == 0 and puntos_bot == 0:
        eleccion_bot = random.choice(resultados)
    else:
        if len(set(jugadas_jugador.values())) == 1:
            eleccion_bot = random.choice(resultados)
        else:
            mas_comun = max(jugadas_jugador, key=jugadas_jugador.get)
            eleccion_bot = ganar_a[mas_comun]

    if eleccion_jugador == eleccion_bot:
        texto = "¡Empate!"
    elif ganadores[eleccion_jugador] == eleccion_bot:
        texto = "¡Has ganado la ronda!"
        puntos_jugador += 1
    else:
        texto = "Boti boti ha ganado esta ronda."
        puntos_bot += 1

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

    # 🖼 --- CONFIGURACIÓN DE IMÁGENES ---
    seleccion_jugador.config(image=diccionario_imagenes[eleccion_jugador])
    seleccion_jugador.image = diccionario_imagenes[eleccion_jugador]
    seleccion_bot.config(image=diccionario_imagenes[eleccion_bot])
    seleccion_bot.image = diccionario_imagenes[eleccion_bot]

# 📊 --- MARCADOR Y RESULTADOS ---
def reiniciar_marcador():
    global puntos_bot, puntos_jugador, jugadas_jugador

    puntos_bot = 0
    puntos_jugador = 0

    marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}")
    jugadas_jugador = {" 🪨 Piedra":0, " 📄 Papel":0, " ✂️ Tijera":0}

    seleccion_jugador.config(image=img_vacia)

    seleccion_bot.config(image=img_vacia)

    

#Creación de la ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("850x700")
ventana.configure(bg="#d0f0c0")  

#Insertar imagenes para los botones
img_original_piedra = Image.open("C:\\Users\\alvar\\Desktop\\Proyectos Varios\\Nivel_1\\PiedraPapelTijera\\images\\stone.png")
img_original_papel = Image.open("C:\\Users\\alvar\\Desktop\\Proyectos Varios\\Nivel_1\\PiedraPapelTijera\\images\\toilet-paper.png")
img_original_tijera = Image.open("C:\\Users\\alvar\\Desktop\\Proyectos Varios\\Nivel_1\\PiedraPapelTijera\\images\\scissors.png")
img_original_vacia = Image.open("C:\\Users\\alvar\\Desktop\\Proyectos Varios\\Nivel_1\\PiedraPapelTijera\\images\\question-mark.png")

img_redi_piedra = img_original_piedra.resize((100, 100), Image.Resampling.LANCZOS)
img_redi_papel = img_original_papel.resize((100, 100), Image.Resampling.LANCZOS)
img_redi_tijera = img_original_tijera.resize((100, 100), Image.Resampling.LANCZOS)
img_redi_vacia = img_original_vacia.resize((100, 100), Image.Resampling.LANCZOS)

img_piedra = ImageTk.PhotoImage(img_redi_piedra)
img_papel = ImageTk.PhotoImage(img_redi_papel)
img_tijera = ImageTk.PhotoImage(img_redi_tijera)
img_vacia = ImageTk.PhotoImage(img_redi_vacia)

diccionario_imagenes = {
    " 🪨 Piedra":img_piedra,
    " 📄 Papel":img_papel,
    " ✂️ Tijera":img_tijera
}

# Marcador de la puntuación
marcador = tk.Label(ventana, text="Marcador: ", font=("Helvetica", 14, "bold"), bg="#d0f0c0")
marcador.pack(pady=10)

#Conjunto de botones de opciones
frame_botones = tk.Frame(ventana, bg="#d0f0c0")
frame_botones.pack(pady=20)

piedra = tk.Button(frame_botones, image=img_piedra,  font=("Helvetica", 14, "bold"), command=lambda: jugar(" 🪨 Piedra"), bg="#d0f0c0", fg="white", activebackground="#3e3e5f")
piedra.pack(side="left", padx=10)

papel = tk.Button(frame_botones, image=img_papel, width=100, height=100, font=("Helvetica", 14, "bold"), command=lambda: jugar(" 📄 Papel"), bg="#d0f0c0", fg="white", activebackground="#3e3e5f")
papel.pack(side="left", padx=10)

tijera = tk.Button(frame_botones, image=img_tijera, width=100, height=100,font=("Helvetica", 14, "bold"), command=lambda: jugar(" ✂️ Tijera"), bg="#d0f0c0", fg="white", activebackground="#3e3e5f")
tijera.pack(side="left", padx=10)

#Conjunto de imágenes de resultados
frame_resultados = tk.Frame(ventana, bg="#d0f0c0")
frame_resultados.pack(pady=20)

seleccion_jugador = tk.Label(frame_resultados, image=img_vacia, bg="#d0f0c0")
seleccion_jugador.pack(side="left", padx=10)


seleccion_bot = tk.Label(frame_resultados, image=img_vacia, bg="#d0f0c0")
seleccion_bot.pack(side="left", padx=10)

resultado = tk.Label(ventana, text=f"Resultado:\n\nElegiste: {eleccion_jugador}", font=("Helvetica", 11, ""), bg="#d0f0c0")
resultado.pack(pady=10)

reseteo = tk.Button(ventana, text="Reiniciar Marcador", command=reiniciar_marcador, font=("Helvetica", 14, "bold"), bg="#d0f0c0", fg="black", activebackground="#3e3e5f")
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