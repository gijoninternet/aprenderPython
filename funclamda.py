area_triangulo=lambda b,h:b*h/2

print(area_triangulo(3,4))


numeros=[17,24,7,39,8,51,92]
numero_par=lambda numero:numero%2==0
print(list(filter(numero_par,numeros)))