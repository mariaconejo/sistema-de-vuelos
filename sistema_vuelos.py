# Lista de vuelos
# Almacernar vuelos en un diccionario, separar la informacion usando {} y , 
vuelos = [
    {"id": 1, "fecha": "2025-04-14", "hora": "10:00", "origen": "Alajuela", "destino": "New York", "asientos_disponibles": 5},
    {"id": 2, "fecha": "2025-04-15", "hora": "14:00", "origen": "Alajuela", "destino": "Roma", "asientos_disponibles": 2},
    {"id": 3, "fecha": "2025-04-16", "hora": "23:00", "origen": "Alajuela", "destino": "Paris", "asientos_disponibles": 20},
    {"id": 4, "fecha": "2025-04-17", "hora": "14:00", "origen": "Alajuela", "destino": "Ciudad Panama", "asientos_disponibles": 3},
    {"id": 5, "fecha": "2025-04-18", "hora": "14:00", "origen": "Alajuela", "destino": "Managua", "asientos_disponibles": 4},
    {"id": 6, "fecha": "2025-04-19", "hora": "14:00", "origen": "Alajuela", "destino": "Lima", "asientos_disponibles": 30},
    {"id": 7, "fecha": "2025-04-20", "hora": "14:00", "origen": "Alajuela", "destino": "Ciudad de Mexico", "asientos_disponibles": 10},
    {"id": 8, "fecha": "2025-04-21", "hora": "14:00", "origen": "Alajuela", "destino": "Buenos Aires", "asientos_disponibles": 8},
    {"id": 9, "fecha": "2025-04-22", "hora": "14:00", "origen": "Alajuela", "destino": "Santiago", "asientos_disponibles": 9},
    {"id": 10,"fecha": "2025-04-23", "hora": "14:00", "origen": "Alajuela", "destino": "Madrid", "asientos_disponibles": 50},
    {"id": 11,"fecha": "2025-04-24", "hora": "14:00", "origen": "Alajuela", "destino": "Tokio", "asientos_disponibles": 1}
]


# Lista de reservas
# Almacenar los asientos reservados de vuelos
reservas = []


# Mostrar asientos de vuelos disponibles
def mostrar_vuelos_disponibles():
    print("Vuelos disponibles:")
    for vuelo in vuelos: # Itera sobre cada vuelo dentro del diccionario aninado, la lista vuelos toda la informacion disponible
        print(f"ID: {vuelo['id']}, Fecha: {vuelo['fecha']}, Hora: {vuelo['hora']}, Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Asientos disponibles: {vuelo['asientos_disponibles']}")
        # Mostrar informacion en un print de los vuelos
        


 # Reservar vuelo
def reservar_vuelo():
     nombre_pasajero = input("Ingrese su nombre: ") # Pedir el nombre del pasajero
     mostrar_vuelos_disponibles() # Llamar a la funcion mostar_vuelos_disponibles para que el pasajero observe la lista de vuelos
     id_vuelo = int(input("Ingrese el numero del vuelo que desea reservar: ")) # Usuario ingrese el numero de vuelo
     for vuelo in vuelos: # Iterar sobre cada vuelo en la lista vuelos
            if vuelo["id"] == id_vuelo and vuelo["asientos_disponibles"] > 0:
                vuelo["asientos_disponibles"] -= 1
                reservas.append({"vuelo_id": id_vuelo, "pasajero_nombre": nombre_pasajero})
                print(f"Reserva completada para {nombre_pasajero} en el vuelo ID {id_vuelo}.")
                return
print("No hay asientos disponibles o el ID del vuelo no es válido.")

# Cancelar reserva
def cancelar_reserva():
    nombre_pasajero = input("Ingrese su nombre para cancelar la reserva: ")
    for reserva in reservas:
        if reserva["pasajero_nombre"] == nombre_pasajero:
            for vuelo in vuelos:
                if vuelo["id"] == reserva["vuelo_id"]:
                    vuelo["asientos_disponibles"] += 1
                    reservas.remove(reserva)
                    print(f"Reserva cancelada para {nombre_pasajero}.")
                    return
    print("No se encontró ninguna reserva para ese nombre.")

# Menú del sistema
def menu():
    opcion = 0;
    while opcion != 4:
        print("\n--- Sistema de Reservas de Vuelos ---")
        print("1. Ver vuelos disponibles")
        print("2. Reservar vuelo")
        print("3. Cancelar reserva")
        print("4. Salir")

        opcion = int(input("Selecciona una opcion del menu (1/2/3): "));
        
        if opcion == "1":
            mostrar_vuelos_disponibles()
        elif opcion == "2":
            reservar_vuelo()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el sistema
menu()
