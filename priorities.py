def get_priority(color):
    priorities={"Rojo":"Importante", "Amarillo":"Prioridad Media", "Verde":"Prioridad Baja"} 
    return priorities.get(color,"Sin prioridad")
# Devuelve True
assert  get_priority("Rojo")=="Importante","Error, el color no es equivalente a la prioridad"  
