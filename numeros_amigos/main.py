"""
Al final se encuentra una sección con casos de prueba. Por defecto, utiliza el caso de 100000, 
para utilizar otro, comentar la línea de ejecución y descomentar el caso que se quiera utilizar.

"""


import time

def amigos(MAX):
  inicio_cronometro = time.time()
  for numero_actual in range(MAX):
      suma_divisores_1 = 0
      raiz_1 = int(numero_actual**0.5)

      for divisor in range(1, raiz_1 + 1):
          if numero_actual % divisor == 0:
              suma_divisores_1 += divisor
              if numero_actual // divisor != divisor and numero_actual // divisor != numero_actual:
                  suma_divisores_1 += numero_actual // divisor

      if suma_divisores_1 >= numero_actual:
            suma_divisores_2 = 0
            raiz_2 = int(suma_divisores_1**0.5)

            for divisor_2 in range(1, raiz_2 + 1):
                if suma_divisores_1 % divisor_2 == 0:
                    suma_divisores_2 += divisor_2
                    if suma_divisores_1 // divisor_2 != divisor_2 and suma_divisores_1 // divisor_2 != suma_divisores_1:
                        suma_divisores_2 += suma_divisores_1 // divisor_2

            if suma_divisores_2 == numero_actual:
                print(numero_actual, suma_divisores_1)

  fin_cronometro = time.time()
  print(fin_cronometro - inicio_cronometro)


# Casos de prueba
#amigos(50000)
amigos(100000)
#amigos(150000)
#amigos(200000)
#amigos(250000)
