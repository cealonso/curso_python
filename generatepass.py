import random
import pyperclip as pc

def generatePassword(x):
    max_chars=0
    if (x=="low"):
        max_chars=8
    elif (x=="middle"):
        max_chars=12
    else:
    		max_chars=16
    lst_char=[]
    character=""
    lst_pass=[]
    lst_char=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","(",")","[","]","$",".","_"]        
    for i in range(max_chars):
        character=random.choice(lst_char) 
        lst_pass.append(character)
    a="".join(lst_pass)    
    return a
    
passw=[]
level_security=input("Ingrese el nivel de la contraseña(low/middle/high) : ")
passw=generatePassword(level_security)
print(passw)
pc.copy(passw)




