user_name=input("¿Cuál es su nombre? ")
greetings = [
    "¡Hola!",
    "¡Buenos días!",
    "¡Buenas tardes!",
    "¡Buenas noches!",
    "¡Qué tal!",
    "¡Saludos!",
    "¡Hey!",
    "¿Cómo estás?"
]

greetings.append("¿Cómo Te va?")
greetings.append("¿Qué hay de nuevo? ")

print(greetings)
print(type(greetings))

print(greetings[4]+" "+user_name)