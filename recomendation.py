user_name=input("¿Cuál es su nombre? ")
hobbies=[]
hobby=input("¿Dime algún gusto tuyo, (bye es la despedida) "+ user_name + "? ") 
if (hobby.upper()=="Ver peliculas".upper()):
    hobbies.append("Ver Estrenos de Cine")
    hobbies.append("Leer libros de Filmografías")
if (hobby.upper()=="Comer pizzas".upper()):
    hobbies.append("Comer Hamburguesas")
    hobbies.append("Escuchar Musica")
if (hobby.upper()=="bye".upper()):
    print("Nos vemos!")
print(hobbies)