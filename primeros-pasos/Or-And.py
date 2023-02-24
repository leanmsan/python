#Operadores and y or

usuario_logueado = False
usuario_admin = False

if usuario_logueado and usuario_admin :
    print("Usuario Administrador")
elif usuario_logueado:
    print("Acceso al Sistema")
else :
    print("Debes iniciar sesion")


if usuario_logueado or usuario_admin :
    print("Usuario Administrador")
elif usuario_logueado:
    print("Acceso al Sistema")
else :
    print("Debes iniciar sesion")