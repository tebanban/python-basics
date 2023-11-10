
import random
number= random.randint(1, 10)
intentosRealizados = 0

name=(input("Hola! ¿como te llamas?"))
print("Bueno " + name +" estoy pensando un numero entre 1 y 10 ...")

while intentosRealizados < 5:
  print("trata de adivinar")
  guess=int(input())
  intentosRealizados= intentosRealizados+1

  if guess < number:
      print("Adivina un número mayor...")

  if guess > number:
      print("adivina un número menor...")

  if guess == number:
          break


if guess == number:
    print(" Adivinaste, si era el número...", number )

if guess != number:
    print( "Lo siento, no lo lograste en", intentosRealizados, "intentos, el número era...", number)




    



