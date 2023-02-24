#Evaluar un elemento de la lista
lenguajes = ["Python", "Java", "JavaScript", "R", "PHP"]

if "PHP" in lenguajes: 
    print("Si existe en la lista")
else :
    print("No Esta en la lista")

#IF anidados 
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print("Acceso Total")
    else:
        print("Acceso al sistema")
else :
    print("Debes iniciar sesion")
