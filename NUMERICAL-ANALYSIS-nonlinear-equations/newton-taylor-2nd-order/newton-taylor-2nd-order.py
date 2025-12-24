from math import sin,cos,exp,sqrt
import matplotlib.pyplot as plt


def g(x):
    return x*x - 2
def g_prime(x):
    return 2*x
def g_second(x):
    return 2

def newton_second(f,f_prime,f_second,x0,tol):
    iter = 0
    while abs(f(x0))>tol:
        if (f_prime(x0))**2-2*f_second(x0)*f(x0)>=0:

            numerator = -f_prime(x0)-sqrt((f_prime(x0))**2-2*f_second(x0)*f(x0)) 

            denominator = f_second(x0) 
            x0 += numerator/denominator
            iter += 1
        else:
            x0 += 0.01
    return x0

print(newton_second(g,g_prime,g_second,10,10**(-8)))
