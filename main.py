import inventario
from database import crear_tabla

def mostrar_menu():
    print("\n" + "=======================================")
    print(" 📦 SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=======================================")
    print("1. Agregar nuevo producto")
    print("2. Ver todos los productos")
    print("3. Actualizar stock de un producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=======================================")

def iniciar_programa():
    # Nos aseguramos de que la tabla exista antes de operar
    crear_tabla()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n--- Agregar Producto ---")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio unitario ($): "))
            except ValueError:
                print("❌ Error: Cantidad y precio deben ser valores numéricos.")
                continue
            categoria = input("Categoría: ")
            
            inventario.agregar_producto(nombre, cantidad, precio, categoria)
            
        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            productos = inventario.obtener_productos()
            if not productos:
                print("⚠️ No hay productos registrados en el sistema.")
            else:
                print(f"{'ID':<5} | {'Nombre':<20} | {'Cantidad':<10} | {'Precio ($)':<10} | {'Categoría':<15}")
                print("-" * 68)
                for p in productos:
                    print(f"{p[0]:<5} | {p[1]:<20} | {p[2]:<10} | ${p[3]:<9.2f} | {p[4]:<15}")
                    
        elif opcion == "3":
            print("\n--- Actualizar Stock ---")
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                nueva_cant = int(input("Nueva cantidad de stock: "))
                inventario.actualizar_stock(id_prod, nueva_cant)
            except ValueError:
                print("❌ Error: Ingrese números válidos para el ID y la cantidad.")
                
        elif opcion == "4":
            print("\n--- Eliminar Producto ---")
            try:
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_prod)
            except ValueError:
                print("❌ Error: Ingrese un ID numérico válido.")
                
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el Sistema de Inventario! Hasta luego.")
            break
        else:
            print("❌ Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    iniciar_programa()