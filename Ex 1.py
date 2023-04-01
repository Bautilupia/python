"""Ingresar 3 valores correspondientes a la longitud de los lados de un triángulo
Informar:
a - Si los valores ingresados forman un triángulo
b - Si se forma un triángulo, que triángulo es?"""


""" if t1+t2 > t3:
                print("Es un triángulo")"""

t1=int(input("Inserte valor primer lado:"))
t2=int(input("Inserte valor segundo lado:"))
t3=int(input("Inserte valor tercer lado:"))



if t1+t2 < t3:
        print("No es un triángulo")
else:                       
        if t1 and t2 == t3:
                print("Es un triángulo equilátero")
        else:
                if t1==t2:
                        print("Es un triángulo isósceles")
                else:
                        if t1 != t2 != t3:
                                Sprint("Es un triángulo escaleno")
