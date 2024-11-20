# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:18:44 2024

@author: Raul-CDH
"""

##Halla la expresi´on binaria, ternaria, octal y hexadecimal de 12345
#y 177130.
bin(12345)
bin(177130)
hex(12345)
hex(177130)
oct(12345)
oct(177130)

# Calcula la factorizaci´on en primos de los siguientes enteros:
# 39, 81, 88, 101, 126, 143, 289, 512, 729, 899, 1001, 1111, 909090
#
from sympy import factorint
lista = [39, 81, 88, 101, 126, 143, 289, 512, 729, 899, 1001, 1111, 909090]
for i in lista:
    print(f"Factores primos de {i}: {factorint(i)}")

from sympy import gcd
"""
    Utiliza el algoritmo de Euclides para calcular
    mcd(1529, 14038) • mcd(11111, 111111)

"""
print(f"mdc de 1529, 14038: {gcd(1529, 14038)}")
print(f"mdc de 11111, 1111118: {gcd(11111, 111111)}")

"""
    Expresa el m´aximo com´un divisor de cada uno de los siguientes
    pares de enteros como combinaci´on lineal (entera) de ellos
"""
#• (56, 27) 
#(721, 448)
#(3454, 4666)
def egcd(a, b):
    x, X = 0, 1 #inicialización de x1, x0 (según teoría)
    y, Y = 1, 0 #ídem de y1, y0
    while (b != 0):
        B = b
        q = a // b
        a, b = b, a % b
        x, X = X - q * x, x
        y, Y = Y - q * y, y
    return ([B, X, Y])
print(f"combinacion lineal de (55,27)= {egcd(56, 27)}")
print(f"combinacion lineal de (721, 448)= {egcd(721, 448)}")
print(f"combinacion lineal de (721, 448)= {egcd(3454, 4666)}")
 
#9.  Calcula la funci´on Phi de Euler para todos los enteros
#   considera-dos en el problema 3.
#
from sympy import totient
lista = [39, 81, 88, 101, 126, 143, 289, 512, 729, 899, 1001, 1111, 909090]
for i in lista:
    print(f"φ({i}) = {totient(i)}")

#10. Calcula el inverso de 13 m´odulo 17 y m´odulo 2436.
from sympy import mod_inverse
a = 13
modulo = [17,2436]
for i in modulo:
    print(f"El inverso modular de {a} mod {i} es: {mod_inverse(a,i)}")

from sympy import gcdex
#12. Resuelve las siguientes congruencias lineales
#a) 6x ≡ 0 (mod 15)
gcd,x,y = gcdex(6,15)
print(f"6 * {x} ≡ 0 (mod 15)")
#b) 4x ≡ 1 (mod 15)
gcd,x,y = gcdex(4,15)
print(f"4 * {x} ≡ 1 (mod 15)")
#c) 6x ≡ 3 (mod 15)
gcd,x,y = gcdex(6,15)
print(f"6 * {x} ≡ 3 (mod 15)")
#d)) 6x ≡ 5 (mod 15)
gcd,x,y = gcdex(6,15)
print(f"6 * {x} ≡ 5 (mod 15)")

#e) 6x ≡ 1 (mod 15)
gcd,x,y = gcdex(6,15)
print(f"6 * {x} ≡ 1 (mod 15)")

#13 Halla todas las soluciones del sistema de congruencias
from sympy import mod_inverse
# x ≡ 1 (mod 2)
# x ≡ 2 (mod 3)
# x ≡ 3 (mod 5)
# x ≡ 4 ( mod 11)

#hallamos el producto de los modulos
M = 2*3*5*11
#hallar el cociente de cada Mi
M1 = int(M/2)
M2 = int(M/3)
M3 = int(M/5)
M4 = int(M/11)
#hallar los inversos modulares

N1 = mod_inverse(M1, 2)
N2 = mod_inverse(M2, 3)
N3 = mod_inverse(M3, 5)
N4 = mod_inverse(M4, 11)

#hallar valor de X
a1 = 1  
a2 = 2
a3 = 3
a4 = 4
x = ((a1 * M1 * N1) + (a2 * N2 * M2) + (a3 * N3 * M3))
# el resultado lo dividimos entre M
resto = x % M
print(f"el resultado es {resto}")

from sympy.ntheory.modular import crt
restos =[1,2,3,4]
modulos = [2,3,5,11]
solcucion, modulocomun = crt(restos,modulos)
print(f"La solución del sistema de congruencias es: {solcucion} (mod {modulocomun})")

#15. 15 Calcula 19 ^83 (mod 91)
resultado = pow(19,83,91)
print(f"el resultado es {resultado}")

