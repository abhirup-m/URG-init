#!/bin/python
import pprint
from sympy.matrices import Matrix
from sympy import *
U, t= symbols("U t")

U=1
t=2
d = sqrt(U**2+16*t**2)
H = Matrix([[0,t,0,-t],[t,U,-t,0],[0,-t,0,t],[-t,0,t,U]])
id = Matrix([[1,0],[0,1]])
np = d*(d+U)
nm = d*(d-U)
zero = Matrix([[0,0],[0,0]])
#P1 = Matrix([[-id,id],[id,id]])/sqrt(2)
u = Matrix([[4*t/nm, 4*t/np],[(U-d)/nm,(U+d)/np]])
u2 = Matrix([[4*t/(U-d), 4*t/(U+d)],[1,1]])
h = Matrix([[(U-d)/2,0,0,0],[0,(U+d)/2,0,0],[0,0,0,0],[0,0,0,U]])
H2 = Matrix([[0,2*t],[2*t,U]])
ut2 = H2.diagonalize()[0]
Ut2 = (1/sqrt(2))*Matrix([[-ut2,id],[ut2,id]])
#pprint(H)
#pprint(H2.diagonalize()[1])
Ut = (1/sqrt(2))*Matrix([[-u,id],[u,id]])
#pprint(ut2)
#pprint(ut2.T)
#P2 = Matrix([[u,zero],[zero,id]])
##H1 = P1.T*H*P1
##H2 = P2.T*H1*P2
#P = P1*P2
##Hb = P.T*H*P
#H2 = Matrix([[0, 2*t],[2*t,U]])
#V1 = H2.eigenvects()[0][2][0]
#V2 = H2.eigenvects()[1][2][0]
#pprint (V1)
#pprint (V2)
A = (1/d)*Matrix([[4*t**2, U],[U, -4*t**2]])
sx = Matrix([[0,1],[1,0]])
a = Matrix([[1,0],[0,0]])
t = Matrix([[a-id, a],[a,a-id]])
tb = Ut**(-1)*t*Ut
pprint(tb)
#pprint(H)
#pprint(Ut.T*H*Ut)
#pprint(tb*Hb)
#pprint(Hb*tb)
