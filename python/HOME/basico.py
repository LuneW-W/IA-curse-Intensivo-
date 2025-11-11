lim_superior=int(input("Ingrese la altura"))
lim_inferior=int(input("Ingrese el largo"))
largo=0
altura=0
while altura<lim_superior:
    print("\n")
    altura=altura+1
    while  largo<lim_inferior:
        print("0 ")
        largo=largo+1

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
