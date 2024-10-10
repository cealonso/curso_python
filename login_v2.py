import datetime
#obtenemos la fecha y la hora actual.
now = datetime.datetime.now()
user_name=input("¿Cuál es su nombre? ")
planet_name=input("¿Cuál es el nombre del planeta? ")
print(type(user_name))
print(type(planet_name))
#convertir una variable str a int
#print(int(planet_name))
print("Bienvenido "+user_name+" del planeta "+planet_name+" se conecto "+now)