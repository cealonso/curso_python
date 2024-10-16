import recomendation2 as rec
import random 
user_name=input('¿Cúal es tu nombre? ')
goodbyes= ["¡Hasta luego!", "¡Adiós!", "¡Nos vemos pronto!", "Cuídate mucho.", "¡Hasta la próxima!", "Que tengas un buen día.",
           "¡Hasta la vista!", "¡Chao!", "¡Nos vemos!", "¡Suerte en todo!"]
hobbies=[]
hobby=""
while (hobby != 'bye'):
    hobby=input("¿Dime algún gusto tuyo, (bye es la despedida) "+ user_name + "? ") 
    rec.suggestion(hobby,hobbies)
    if (hobby.upper()=="bye".upper()):
        break
print("Las sugerencias son: "+str(hobbies)) 
print(random.choice(goodbyes)+" "+user_name)
