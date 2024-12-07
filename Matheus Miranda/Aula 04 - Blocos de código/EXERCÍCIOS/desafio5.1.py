def forma_triangulo(a, b, c):
 
  return a + b > c and a + c > b and b + c > a


lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))


if forma_triangulo(lado1, lado2, lado3):
  print("Os segmentos formam um triângulo.")
else:
  print("Os segmentos não formam um triângulo.")
