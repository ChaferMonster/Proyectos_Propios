import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import font as tkFont

# =============================
# 🎮 --- VARIABLES DEL JUEGO ---
# =============================
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

def iniciar_partida(rondas_objetivo):
    print(f"Iniciando partida de {rondas_objetivo} rondas")


    global rondas_ganadoras
    rondas_ganadoras = rondas_objetivo

    frame_inicio.pack_forget()

    frame_juego.pack(fill="both", expand=True)


    
# =============================
# --- LÓGICA DE JUEGO ---
# =============================
def jugar(eleccion):
    global eleccion_jugador, eleccion_bot, puntos_jugador, puntos_bot
    eleccion_jugador = eleccion
    jugadas_jugador[eleccion_jugador] +=1

    ganadores = {
    " 🪨 Piedra": " ✂️ Tijera",
    " 📄 Papel": " 🪨 Piedra",
    " ✂️ Tijera": " 📄 Papel"
    }

    # =============================
    # 🤖 --- LÓGICA DE LA IA ---
    # =============================
    probabilidad = random.randint(1,10)
    if puntos_jugador >= puntos_bot:
        

        if probabilidad <= 2:
            eleccion_bot = random.choice(resultados)
        else:
            if puntos_jugador == 0 and puntos_bot == 0:
                eleccion_bot = random.choice(resultados)
            else:
                if len(set(jugadas_jugador.values())) == 1:
                    eleccion_bot = random.choice(resultados)
                else:
                    mas_comun = max(jugadas_jugador, key=jugadas_jugador.get)
                    eleccion_bot = ganar_a[mas_comun]
    else:
        if probabilidad <= 5:
            eleccion_bot = random.choice(resultados)
        else:
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

    if puntos_jugador == rondas_ganadoras:
        messagebox.showinfo(
        f"¡Has ganado!", "ENHORABUENA"
    )
        frame_juego.pack_forget()
        frame_inicio.pack(fill="both", expand=True)
        reiniciar_marcador()

    elif puntos_bot == rondas_ganadoras:
        messagebox.showinfo(
        f"Boti boti te a destrozado!","Perdedor"
    )
        frame_juego.pack_forget()
        frame_inicio.pack(fill="both", expand=True)
        reiniciar_marcador()

    # =============================
    # 🖼 --- CONFIGURACIÓN DE IMÁGENES ---
    # =============================
    seleccion_jugador.config(image=diccionario_imagenes[eleccion_jugador])
    seleccion_jugador.image = diccionario_imagenes[eleccion_jugador]
    seleccion_bot.config(image=diccionario_imagenes[eleccion_bot])
    seleccion_bot.image = diccionario_imagenes[eleccion_bot]
    

def parpadeo(widget, veces=4):
    if veces > 0:
        color = "#f4a261" if veces % 2 == 0 else "black"
        widget.config(fg=color)
        ventana.after(200, parpadeo, widget, veces - 1)

# =============================
# 📊 --- MARCADOR Y RESULTADOS ---
# =============================
def reiniciar_marcador():
    global puntos_bot, puntos_jugador, jugadas_jugador

    puntos_bot = 0
    puntos_jugador = 0

    marcador.config(text=f"Marcador:\n\n Tu: {puntos_jugador}  -  {puntos_bot}")
    jugadas_jugador = {" 🪨 Piedra":0, " 📄 Papel":0, " ✂️ Tijera":0}

    seleccion_jugador.config(image=img_vacia)

    seleccion_bot.config(image=img_vacia)

    mensaje_reinicio = tk.Label(reinicio_frame, text="¡Nueva partida!", font=("Arial", 20, "bold"), bg="#d0f0c0", fg="#f4a261")
    mensaje_reinicio.pack()
    ventana.after(1500, mensaje_reinicio.destroy)

    parpadeo(marcador)

# =============================
# --- FUNCIONES PARA RESALTAR BOTONES ---
# =============================
def hover_in(event):
    event.widget.config(bg="#e0e0e0")

def hover_out(event):
    event.widget.config(bg="#80a070")

    
# =============================
#Creación de la ventana
# =============================
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("850x900")
ventana.configure(bg="#d0f0c0") 

bg_image = Image.open("C:\\Users\\alvar\\Desktop\\Proyectos Varios\\Nivel_1\\PiedraPapelTijera\\images\\fondo.png")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(ventana, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# =============================
# Fuente personalizada para el título
# =============================
titulo_fuente = tkFont.Font(family="Comic Sans MS", size=32, weight="bold")

# =============================
# Función hover para botones
# =============================
def on_enter(e):
    e.widget['background'] = "#81c784"  # más oscuro al pasar
    e.widget['fg'] = "white"

def on_leave(e):
    e.widget['background'] = "#4caf50"  # color original
    e.widget['fg'] = "black"

frame_inicio = tk.Frame(ventana, bg="#d0f0c0")
frame_inicio.pack(fill="both", expand=True)

inicio = tk.Label(frame_inicio, text="Piedra, Papel o Tijera con IA",
                  font=titulo_fuente, bg="#d0f0c0", fg="#f4a261").pack(pady=20)

sombra = tk.Frame(frame_inicio, bg="#a0b48c")
sombra.pack(padx=(15, 0), pady=(15, 0))

frame_dificultad = tk.Frame(sombra, bg="#b8d8a5", bd=2, relief="groove", padx=10, pady=10)
frame_dificultad.pack(padx=10, pady=10)

# Lista de botones
opciones = [
    ("[ Fácil (3 rondas) ]", 3),
    ("[ Normal (5 rondas) ]", 5),
    ("[ Difícil (10 rondas) ]", 10)
]

for texto, rondas in opciones:
    btn = tk.Button(frame_dificultad, text=texto,
                    font=("Helvetica", 16, "bold"),
                    bg="#4caf50", fg="black",
                    activebackground="#388e3c", activeforeground="white",
                    command=lambda r=rondas: iniciar_partida(r))
    btn.pack(pady=10, ipadx=10, ipady=5)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)


# =============================
#Insertar imagenes para los botones
# =============================
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

frame_juego = tk.Frame(ventana,bg="#d0f0c0")

reinicio_frame = tk.Frame(frame_juego, bg="#d0f0c0")
reinicio_frame.pack()

# =============================
# Marcador de la puntuación
# =============================
marcador = tk.Label(frame_juego, text="Marcador: ", font=("Helvetica", 14, "bold"), bg="#d0f0c0", fg="#003300")
marcador.pack(pady=10)

# =============================
#Conjunto de botones de opciones
# =============================
frame_botones = tk.Frame(frame_juego, bg="#a0c090")
frame_botones.pack(pady=20)

piedra = tk.Button(frame_botones, image=img_piedra,  font=("Helvetica", 14, "bold"), command=lambda: jugar(" 🪨 Piedra"), bg="#80a070", fg="white", activebackground="#3e3e5f")
piedra.bind("<Enter>", hover_in)
piedra.bind("<Leave>", hover_out)
piedra.pack(side="left", padx=10)

papel = tk.Button(frame_botones, image=img_papel, width=100, height=100, font=("Helvetica", 14, "bold"), command=lambda: jugar(" 📄 Papel"), bg="#80a070", fg="white", activebackground="#3e3e5f")
papel.bind("<Enter>", hover_in)
papel.bind("<Leave>", hover_out)
papel.pack(side="left", padx=10)

tijera = tk.Button(frame_botones, image=img_tijera, width=100, height=100,font=("Helvetica", 14, "bold"), command=lambda: jugar(" ✂️ Tijera"), bg="#80a070", fg="white", activebackground="#3e3e5f")
tijera.bind("<Enter>", hover_in)
tijera.bind("<Leave>", hover_out)
tijera.pack(side="left", padx=10)

# =============================
#Conjunto de imágenes de resultados
# =============================
frame_resultados = tk.Frame(frame_juego, bg="#a0c090")
frame_resultados.pack(pady=20)

seleccion_jugador = tk.Label(frame_resultados, image=img_vacia, bg="#a0c090")
seleccion_jugador.grid(row=0, column=0, pady=5, padx=10)
tk.Label(frame_resultados, text="Jugador", font=("Arial", 14, "bold", ), bg="#a0c090").grid(row=1, column=0, pady=5)


seleccion_bot = tk.Label(frame_resultados, image=img_vacia, bg="#a0c090")
seleccion_bot.grid(row=0, column=1, pady=5, padx=10)
tk.Label(frame_resultados, text="Boti boti", font=("Arial", 14, "bold"), bg="#a0c090").grid(row=1, column=1, pady=5)

resultado = tk.Label(frame_juego, text=f"Resultado:\n\nElegiste: {eleccion_jugador}", font=("Helvetica", 11, ""), bg="#d0f0c0", fg="#003300")
resultado.pack(pady=10)

reseteo = tk.Button(frame_juego, text="Reiniciar Marcador", command=reiniciar_marcador, font=("Helvetica", 14, "bold"), bg="#80a070", fg="#f4a261", activebackground="#3e3e5f")
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