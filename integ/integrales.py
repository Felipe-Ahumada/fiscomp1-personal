import numpy as np

def rectangular(f,a,b):
    """Regla del rectangulo"""
    return f(a)*(b-a)
#Definí la regla del rectangulo


#Pon 2 espacios entre 2 definiciones para que quede bonito y lo otro
#es poner una linea larga
#---------------------------------------------------------------
def trapezoidal(f,a,b):
    """regla trapezoidal"""
    return 0.5 * (f(a)+f(b)) * (b-a)

#---------------------------------------------------------------

f = lambda x:(x-1)*np.exp(x)

def midpoint_simple(f,a,b):
    """regla del punto medio"""
    return (b-a)*f((a+b)/2)