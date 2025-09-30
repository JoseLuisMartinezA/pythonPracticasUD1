def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    if edad is None:
        mensaje = f"{nombre} y le gusta: "
    else:
        mensaje = f"{nombre} tiene {edad} años y le gusta: "
    
    if aficiones:
        mensaje += ", ".join(aficiones)
    else:
        mensaje += "no ha especificado aficiones"
    
    print(mensaje)

# Pruebas con diferentes números de aficiones
presentar_persona("Ana", 25, "leer", "correr", "viajar")
presentar_persona("Carlos", 30, "fútbol")
presentar_persona("María")
presentar_persona("Luis", 35, "pintar", "nadar")
presentar_persona()
presentar_persona("Sofia", 28)
presentar_persona("Pedro", 40, "cine", "música", "deporte", "cocina")