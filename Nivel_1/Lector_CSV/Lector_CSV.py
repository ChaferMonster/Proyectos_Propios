import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

archivo_csv = ""

def seleccionar_csv():
    global archivo_csv

    # Selecciona el archivo que queramos
    archivo_csv = filedialog.askopenfilename(
        title="Selecciona un archivo CSV",
        filetypes=[("csv files", "*.csv")]
    )
    if archivo_csv:
        etiqueta_ruta.config(text=f"Archivo seleccionado:\n{archivo_csv}")

    # Carga el archivo como un dataframe
    df = pd.read_csv(archivo_csv)

    # Limpia cualquier dato previo por si añadimos otro csv luego
    arbol.delete(*arbol.get_children())

    # Le dice al Treeview que las columnas visuales deben ser iguales a las del CSV
    arbol["columns"] = list(df.columns)

    # Oculta la primera fila vacia, Treeview pone una fila fantasma por defecto
    arbol["show"] = "headings"

    for _, row in df.iterrows():
        arbol.insert("", "end", values=list(row))


ventana = tk.Tk()
ventana.title("Lector de CSV")
ventana.geometry("600x300")

boton_cargar = tk.Button(ventana, text="📂 Seleccionar CSV", command=seleccionar_csv)
boton_cargar.pack()

etiqueta_ruta = tk.Label(ventana, text="No se ha seleccionado ningún archivo")
etiqueta_ruta.pack()

arbol = ttk.Treeview(ventana, height=10)
arbol.pack()

ventana.mainloop()