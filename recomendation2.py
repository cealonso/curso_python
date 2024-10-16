   
def suggestion(hobby,hobbies):   
    if (hobby.upper()=="Ver Peliculas".upper()):
        hobbies.append("Ver estrenos de cine")
        hobbies.append("Mirar Series")
    if (hobby.upper()=="Comer pizzas".upper()):
        hobbies.append("Comer Hamburguesas")
        hobbies.append("Escuchar Musica")
    if (hobby.upper()=="Aire Libre".upper() or hobby.upper()=="naturaleza".upper()):
        hobbies.append("Andar en bicicleta")
        hobbies.append("Correr")
    return hobbies