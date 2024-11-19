# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:42:12 2024

@author: Raul-CDH
"""

#1 Escribe un bucle que calcule la suma de todos los números pares entre 300 y 3000.
total = 0;
for i in  range(300,3000):
    total += i;
print(total);

#2 Mediante un bucle, haz una lista con todos los números enteros entre 1 y 300 que sean
#múltiplos de 7 y cuyo cuadrado esté comprendido entre 300 y 100000.
lista = []
for i in  range(1,300):
    if (i % 7 == 0) and (300 <= i * i <= 100000) :
        lista.append(i);
        
#3. Usar un bucle while para hallar el menor múltiplo de 137 mayor que 1200.
i = 1200;
while i % 137!=0:
    i+=1;
print(f"El menor múltiplo de 137 es 1200 * {i}");


#4. El juego infantil “piedra, papel o tijera” consiste en que dos jugadores eligen
#una de estas tres opciones, y el resultado es que el papel gana a la piedra
#(envolviéndola), la piedra gana a la tijera (rompiéndola), y la tijera gana al
#papel (cortándolo).
#Escribe un código en Python que decida el ganador a partir del valor de dos
#variables jugador (input), ordenador (aleatorio) que pueden tomar los
#valores “piedra”, “papel”, o “tijera”, y que imprima por pantalla un mensaje
#(print) diciendo si el jugador ha ganado o perdido, y la elección efectuada
#por el ordenador.

import random
reglas = {"piedra":"tijera","papel":"piedra","tijera":"papel"}
flag = True
jugador = " ";
ordenador = " ";
while flag:
   ordenador = random.choice(list(reglas.values()))
   jugador = input("qué eliges?: ");
   if reglas[ordenador] == jugador:
       print("perdiste!! ")
       
   elif reglas[jugador] == ordenador:
       print("Ganaste!! ")
   else:
       print("Empeate!! ")
   flag = True if input("¿Volver a intentar? Pulsa 1 si deseas o 0 en caso contrario: ") == "1" else False

    
    
        
        