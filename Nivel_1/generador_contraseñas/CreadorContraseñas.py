import tkinter as tk
import string
import random
from tkinter import messagebox

ventana = tk.Tk() # Esto crea la ventana
ventana.title("Generador de Contraseñas")

tk.Label(ventana, text="Introduce un sitio web").pack() # Los Label son etiquetas de texto
entrada_sitio = tk.Entry(ventana) # Los Entry son cuadros para escribir texto de entrada
entrada_sitio.pack() # Tanto los Label como Entry se les debe poner .pack()

tk.Label(ventana, text="Longitud de la contraseña").pack()
longitud=tk.Entry(ventana)
longitud.pack()

def generar_contraseña(): # Función para generar una contraseña aleatoria
    long_contraseña = int(longitud.get()) # .get coge lo que se le pide, en este caso es la longitu de la cointraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation # Esta variable añade letras, simbolos y digitos. 
    contraseña = ''.join(random.choice(caracteres) for _ in range(long_contraseña)) # Añade un caracter por cada distancia de longitud de contraseña
    entry_resultado.delete(0, tk.END) # Elimina lo que hubiese previemente. Aunque sea vacío
    entry_resultado.insert(0, contraseña) # Añade la contraseña creada
tk.Button(ventana, text="Generar contraseña", command=generar_contraseña).pack() #Botón en interfaz que permite ejecutar la función

entry_resultado = tk.Entry(ventana, width=30)
entry_resultado.pack()

def guardar_contraseña(): # Función para guardar la contraseña en un txt
    sitio = entrada_sitio.get()
    contraseña = entry_resultado.get()
    if sitio and contraseña:
        with open("contraseñas.txt", "a") as f:
            f.write(f"{sitio}:{contraseña}\n")
        messagebox.showinfo("Guardado", "Contraseña guardada con éxito.") # Pop up con el mensaje indicado
    else:
        messagebox.showwarning("Error", "Introduce un sitio y genera una contraseña.") # Pop up con el mensaje indicado si falla el anterior

tk.Button(ventana, text="Guardar contraseña", command=guardar_contraseña).pack()

ventana.mainloop()
