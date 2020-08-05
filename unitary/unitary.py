#!/bin/python
import pprint
from sympy.matrices import Matrix
from sympy import *
U, t= symbols("U t")

U=0.932
t=0.578
d = sqrt(U**2+16*t**2)
H = Matrix([[0,t,0,-t],[t,U,-t,0],[0,-t,0,t],[-t,0,t,U]])
id = Matrix([[1,0],[0,1]])
zero = Matrix([[0,0],[0,0]])
P1 = Matrix([[-id,id],[id,id]])/sqrt(2)
u = Matrix([[4*t/(U-d), 4*t/(U+d)],[1,1]])
P2 = Matrix([[u,zero],[zero,id]])
H1 = P1.T*H*P1
H2 = P2.T*H1*P2
P = P1*P2
Hb = P.T*H*P
pprint (Hb)
