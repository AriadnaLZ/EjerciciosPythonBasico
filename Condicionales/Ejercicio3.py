# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.

a = 1
b = 2
c = 3
mayor = 0

if a > b and a > c:
  mayor = a
  print(mayor)
elif b > a and b > c:
  mayor = b 
  print(mayor)
elif c > a and c > b:
  mayor = c 
  print(mayor)