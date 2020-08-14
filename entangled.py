#!/bin/python
import sympy
import pprint
from sympy import I, Matrix, symbols
from sympy.physics.quantum import TensorProduct
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc
font = {'size'   : 22}
rc('font', **font)

#x,a,y = symbols("x a y")
#a = 1/(sympy.sqrt(x**2 + 1) -x)
#y = (1/(1+1/a**2))*(sympy.log(2+2/a**2) + sympy.log(2+2*a**2)/a**2)
#pprint(y)
x = np.arange(0,30,0.1)
alpha = (np.sqrt(x**2 + 1) -x)**(-1)
y = (np.log(2 + 2*alpha**(-2)) + np.log(2 + 2*alpha**2)*alpha**(-2))/(1+alpha**(-2))
y1 = (np.log(2 + 2*alpha**(-2)))/(1+alpha**(-2))
y2 = (np.log(2 + 2*alpha**2)*alpha**(-2))/(1+alpha**(-2))
plt.plot(x,y)
plt.plot(x,y1,label="singlet")
plt.plot(x,y2,label="dob-hol")
plt.xlabel(r"$\frac{U}{4t}$")
plt.ylabel(r"entropy of $\rho_1$")
plt.axhline(sympy.log(2),0,21,color="r",label=r"$\log 2$",ls="--")
plt.axhline(sympy.log(4),0,21,color="g",label=r"$\log 4$",ls="--")
plt.legend()
plt.show()

#a = np.array([1,0,0,0])
#b = np.array([0,1,0,0])
#c = np.array([0,0,1,0])
#d = np.array([0,0,0,1])
#prod = np.kron(np.outer(a,a),np.outer(b,b)) + np.kron(np.outer(b,b),np.outer(a,a)) + 1.3*(np.kron(np.outer(c,c),np.outer(d,d)) + np.kron(np.outer(d,d),np.outer(c,c)))
#print (np.trace(prod))

