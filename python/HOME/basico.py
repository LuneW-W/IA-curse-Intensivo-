
#ciclo for
lista_2l=[1,2,3,4,4,5,5,6,7]

for i in lista_2l:
    print(i)

#funcion
def buscar(num,lista):
    x=0
    while num != lista[x] :
        x=x+1
    print(f"el se encontro el numero {num} en la posicion {x+1} ")

lista=[1,2,3,4,4,5,5,6,7] 
numero_bus=int(input("poner numero\n"))
loco=buscar(numero_bus,lista)
print(loco)
#uso class como structer
class usuario:
    def __init__(self,nombre,edad,documento):
        self.nombre= nombre
        self.edad= edad
        self.documento= documento
        pass

nombre_ing= input("Ingrese su nombre\n")
nombre_ing=int(input("Ingrese su edad\n"))
documento_ing=int(input("Ingrese su documento"))

mi_usuario=usuario(nombre_ing,nombre_ing,documento_ing)

print(f"{mi_usuario.documento}")

# condicionales

if