from database import conectar

def agregar_producto(nombre, cantidad, precio, categoria):
    """Agrega un nuevo producto a la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
        INSERT INTO productos (nombre, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?)
    ''', (nombre, cantidad, precio, categoria))
    
    conexion.commit()
    conexion.close()
    print(f"\n✅ Producto '{nombre}' agregado exitosamente.")

def obtener_productos():
    """Devuelve todos los productos registrados."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    
    conexion.close()
    return productos

def actualizar_stock(id_producto, nueva_cantidad):
    """Actualiza la cantidad disponible de un producto."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''
        UPDATE productos
        SET cantidad = ?
        WHERE id = ?
    ''', (nueva_cantidad, id_producto))
    
    conexion.commit()
    conexion.close()
    print(f"\n🔄 Stock del producto ID {id_producto} actualizado a {nueva_cantidad}.")

def eliminar_producto(id_producto):
    """Elimina un producto de la base de datos por su ID."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    
    conexion.commit()
    conexion.close()
    print(f"\n🗑️ Producto ID {id_producto} eliminado correctamente.")