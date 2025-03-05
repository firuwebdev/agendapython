import sqlite3
from tkinter import *
from tkinter import messagebox


# Conectar a la base de datos
def conectar():
    return sqlite3.connect('agenda_clientes.db')


# Crear la tabla si no existe
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        numero TEXT NOT NULL,
        fecha TEXT NOT NULL,
        horario TEXT NOT NULL
    )
    ''')
    conexion.commit()
    conexion.close()

# Función para agregar un cliente
def agregar_cliente():
    nombre = entry_nombre.get()
    numero = entry_numero.get()
    fecha = entry_fecha.get()
    horario = entry_horario.get()

    if nombre and numero and fecha and horario:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute('''
        INSERT INTO clientes (nombre, numero, fecha, horario)
        VALUES (?, ?, ?, ?)
        ''', (nombre, numero, fecha, horario))
        conexion.commit()
        conexion.close()
        messagebox

import sqlite3
from tkinter import *
from tkinter import messagebox

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect('agenda_clientes.db')

# Función para agregar un cliente
def agregar_cliente():
    nombre = entry_nombre.get()
    numero = entry_numero.get()
    fecha = entry_fecha.get()
    horario = entry_horario.get()

    if nombre and numero and fecha and horario:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute('''
        INSERT INTO clientes (nombre, numero, fecha, horario)
        VALUES (?, ?, ?, ?)
        ''', (nombre, numero, fecha, horario))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Cliente agregado con éxito!")
        limpiar_campos()  # Limpiar campos después de agregar
        mostrar_clientes()  # Actualizar la lista
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Función para mostrar todos los clientes
def mostrar_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conexion.close()

    lista_clientes.delete(0, END)  # Limpiar la lista actual
    for cliente in clientes:
        lista_clientes.insert(END, f"ID: {cliente[0]}, Nombre: {cliente[1]}, Número: {cliente[2]}, Fecha: {cliente[3]}, Horario: {cliente[4]}")

# Función para buscar clientes por nombre
def buscar_cliente():
    nombre_busqueda = entry_buscar.get().strip().lower()  # Obtener el nombre a buscar
    if nombre_busqueda:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM clientes WHERE LOWER(nombre) LIKE ?', (f"%{nombre_busqueda}%",))
        clientes = cursor.fetchall()
        conexion.close()

        lista_clientes.delete(0, END)  # Limpiar la lista actual
        for cliente in clientes:
            lista_clientes.insert(END, f"ID: {cliente[0]}, Nombre: {cliente[1]}, Número: {cliente[2]}, Fecha: {cliente[3]}, Horario: {cliente[4]}")
    else:
        mostrar_clientes()  # Mostrar todos los clientes si no hay búsqueda

# Función para cargar los datos del cliente seleccionado en los campos
def cargar_cliente_seleccionado(event):
    cliente_seleccionado = lista_clientes.get(lista_clientes.curselection())  # Obtener el cliente seleccionado
    datos = cliente_seleccionado.split(", ")  # Separar los datos

    # Extraer los valores de los datos
    id = datos[0].split(": ")[1]
    nombre = datos[1].split(": ")[1]
    numero = datos[2].split(": ")[1]
    fecha = datos[3].split(": ")[1]
    horario = datos[4].split(": ")[1]

    # Cargar los valores en los campos de entrada
    entry_nombre.delete(0, END)
    entry_nombre.insert(0, nombre)
    entry_numero.delete(0, END)
    entry_numero.insert(0, numero)
    entry_fecha.delete(0, END)
    entry_fecha.insert(0, fecha)
    entry_horario.delete(0, END)
    entry_horario.insert(0, horario)

    # Guardar el ID del cliente seleccionado para actualizar o eliminar
    global cliente_actual_id
    cliente_actual_id = id

# Función para actualizar un cliente
def actualizar_cliente():
    if cliente_actual_id:
        nombre = entry_nombre.get()
        numero = entry_numero.get()
        fecha = entry_fecha.get()
        horario = entry_horario.get()

        if nombre and numero and fecha and horario:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute('''
            UPDATE clientes
            SET nombre = ?, numero = ?, fecha = ?, horario = ?
            WHERE id = ?
            ''', (nombre, numero, fecha, horario, cliente_actual_id))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Cliente actualizado con éxito!")
            limpiar_campos()  # Limpiar campos después de actualizar
            mostrar_clientes()  # Actualizar la lista
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Error", "Selecciona un cliente para actualizar.")

# Función para eliminar un cliente
def eliminar_cliente():
    if cliente_actual_id:
        confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este cliente?")
        if confirmacion:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_actual_id,))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Cliente eliminado con éxito!")
            limpiar_campos()  # Limpiar campos después de eliminar
            mostrar_clientes()  # Actualizar la lista
    else:
        messagebox.showwarning("Error", "Selecciona un cliente para eliminar.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, END)
    entry_numero.delete(0, END)
    entry_fecha.delete(0, END)
    entry_horario.delete(0, END)
    global cliente_actual_id
    cliente_actual_id = None  # Reiniciar el ID del cliente seleccionado

# Crear la ventana principal
ventana = Tk()
ventana.title("Agenda de Clientes")
ventana.geometry("600x500")

# Variable global para almacenar el ID del cliente seleccionado
cliente_actual_id = None

# Campos de entrada para agregar cliente
Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = Entry(ventana, width=30)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

Label(ventana, text="Número:").grid(row=1, column=0, padx=10, pady=10)
entry_numero = Entry(ventana, width=30)
entry_numero.grid(row=1, column=1, padx=10, pady=10)

Label(ventana, text="Fecha:").grid(row=2, column=0, padx=10, pady=10)
entry_fecha = Entry(ventana, width=30)
entry_fecha.grid(row=2, column=1, padx=10, pady=10)

Label(ventana, text="Horario:").grid(row=3, column=0, padx=10, pady=10)
entry_horario = Entry(ventana, width=30)
entry_horario.grid(row=3, column=1, padx=10, pady=10)

# Botones para agregar, actualizar, eliminar y limpiar
Button(ventana, text="Agregar Cliente", command=agregar_cliente).grid(row=4, column=0, padx=10, pady=10)
Button(ventana, text="Actualizar Cliente", command=actualizar_cliente).grid(row=4, column=1, padx=10, pady=10)
Button(ventana, text="Eliminar Cliente", command=eliminar_cliente).grid(row=4, column=2, padx=10, pady=10)
Button(ventana, text="Limpiar Campos", command=limpiar_campos).grid(row=5, column=1, padx=10, pady=10)

# Campo de búsqueda
Label(ventana, text="Buscar por nombre:").grid(row=6, column=0, padx=10, pady=10)
entry_buscar = Entry(ventana, width=30)
entry_buscar.grid(row=6, column=1, padx=10, pady=10)
Button(ventana, text="Buscar", command=buscar_cliente).grid(row=6, column=2, padx=10, pady=10)

# Lista de clientes
lista_clientes = Listbox(ventana, width=80, height=15)
lista_clientes.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Asignar la función de carga al evento de selección
lista_clientes.bind('<<ListboxSelect>>', cargar_cliente_seleccionado)

# Mostrar todos los clientes al iniciar
mostrar_clientes()

# Ejecutar la ventana
ventana.mainloop()