# Importante, Prioridad Media, Prioridad Baja
#   Rojo          Amarillo         Verde 
#   get_priority()
import datetime
import string
import priorities
        
today = str(datetime.date.today())
count_events=int(input("La cantidad de Eventos que quiero agendar : "))
for t in range(count_events):
  tarea=input("Ingrese el nombre de la tarea: ")
  color=input("ingrese un color de prioridad: (Rojo,Amarillo,Verde) :")
  prior=priorities.get_priority(color)
  with open('task.txt', 'a') as f:
    f.write(today+'\t')
    f.write(str(t)+'\t')
    f.write(tarea+'\t')
    f.write(prior+'\t')
    f.write('\n')