import datetime


Nombre = input("Ingrese su Nombre: ")
Edad = int(input("Ingrese su Edad: "))
fechaHora = datetime.datetime.now()

hora = int(fechaHora.strftime('%H'))


if Edad < 18:
  if hora > 18:
    print("Ve a dormir si hacer nada")
  else:
    print("Realizar tus tareas")
else:
  print("No esta obligado hacer nada")
