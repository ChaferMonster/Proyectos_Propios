import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

archivo_csv = ""
combo_columnas = None

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

    # Para listar las columnas en el Combobox
    columnas = list(df.columns)
    combo_columnas["values"] = columnas
    combo_columnas.current(0)

    # Limpia cualquier dato previo por si añadimos otro csv luego
    arbol.delete(*arbol.get_children())

    # Le dice al Treeview que las columnas visuales deben ser iguales a las del CSV
    arbol["columns"] = list(df.columns)

    # Oculta la primera fila vacia, Treeview pone una fila fantasma por defecto
    arbol["show"] = "headings"

    for _, row in df.iterrows():
        arbol.insert("", "end", values=list(row))

def mostrar_resumen():
    if not archivo_csv:
        return

    ventana_resumen = tk.Toplevel()
    ventana_resumen.title = "Resumen del CSV"
    ventana_resumen.geometry("400x300")

    df = pd.read_csv(archivo_csv)

    resumen_texto = (
        f"Filas: {df.shape[0]}\n"
        f"Columnas: {df.shape[1]}\n"
        f"Columnas: \n{','.join(df.columns)}\n\n"
        f"Nulos por columnas:\n{df.isnull().sum().to_string()}\n\n"
        f"Tipos de datos:\n{df.dtypes.to_string()}"
    )


    text_area = tk.Text(ventana_resumen, wrap="word")
    text_area.insert("1.0", resumen_texto)
    text_area.config(state="disabled")

    scrollbar = tk.Scrollbar(ventana_resumen, command=text_area.yview)

    text_area.config(yscrollcommand=scrollbar.set)

    text_area.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


def analizar_columna(event):
    if not archivo_csv:
        return
    
    columna_seleccionada = combo_columnas.get()
    df = pd.read_csv(archivo_csv)

    valores = df[columna_seleccionada]

    if pd.api.types.is_numeric_dtype(valores):
        resumen = (
            f"Columna: {columna_seleccionada} (numérica)\n"
            f"Media: {valores.mean():.2f}\n"
            f"Mínimo: {valores.min()}\n"
            f"Máximo: {valores.max()}"
        )
    else:
        resumen = (
            f"Columna: {columna_seleccionada} (texto)\n"
            f"Valores únicos: {valores.nunique()}\n"
            f"Más común: {valores.mode().iloc[0]}"
        )

    label_analisis.config(text=resumen)

def contar_valores():
        if not archivo_csv:
            return
        
        df = pd.read_csv(archivo_csv)
        columna_seleccionada = combo_columnas.get()
        conteo = df[columna_seleccionada].value_counts()

        texto = f"Valores únicos en '{columna_seleccionada}':\n \n{conteo.to_string()}"
        label_valores_unicos.config(text=texto)


ventana = tk.Tk()
ventana.title("Lector de CSV")
ventana.geometry("600x300")

boton_cargar = tk.Button(ventana, text="📂 Seleccionar CSV", command=seleccionar_csv)
boton_cargar.pack(pady=10)

boton_resumen = tk.Button(ventana, text="📈 Ver resumen", command=mostrar_resumen)
boton_resumen.pack(pady=10)

etiqueta_ruta = tk.Label(ventana, text="No se ha seleccionado ningún archivo")
etiqueta_ruta.pack()

combo_columnas = ttk.Combobox(ventana, state="readonly")
combo_columnas.bind("<<ComboboxSelected>>", analizar_columna)
combo_columnas.pack(pady=5)

label_analisis = tk.Label(ventana, text="", justify="left")
label_analisis.pack(pady=10)

cuenta_valor = tk.Button(ventana, text="📊 Contar valores únicos", command=contar_valores)
cuenta_valor.bind("<<ComboboxSelected>>", contar_valores)
cuenta_valor.pack(pady=10)

label_valores_unicos = tk.Label(ventana, text="", justify="left")
label_valores_unicos.pack(pady=10)

arbol = ttk.Treeview(ventana, height=10)
arbol.pack()

ventana.mainloop()