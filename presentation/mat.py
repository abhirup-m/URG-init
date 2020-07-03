#!/bin/python
import sympy
from sympy import init_printing
from sympy import *
sympy.init_printing(use_unicode=True)

w,u,k2,q,e,u,u12,u21,k1 = symbols('w u k2 q e u u12 u21 k1')

# A12 means first row, second column
# I is sqrt(-1)
A11 = -I*w+u*k2-q*e*u 
A12 = -u12*k2+q*e*u12
A21 = -u21*k2+q*e*u21
A22 = -I*w+u*k1-q*e*u
B11 = u
B12 = u21
B21 = u12
B22 = u
C11 = I*w+u*k2-q*e*u
C12 = -u21*k2+q*e*u21
C21 = -u12*k2+q*e*u12
C22 = I*w+u*k1-q*e*u

A = Matrix([[A11, A12],[A21, A22]])
B = Matrix([[B11, B12],[B21, B22]])
C = Matrix([[C11, C12],[C21, C22]])

print ("A=",A)
print ("B=",B)
print ("C=",C)

P = A*B*C

print (P)
