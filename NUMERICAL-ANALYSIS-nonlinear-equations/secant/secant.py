import matplotlib.pyplot as plt
from math import sin,exp

def f1(x):
    return x*x*x - x + 1

def f2(x):
    return sin(x) - 0.5

def f3(x):
    return exp(x) - 2

def f4(x):
    return pow(x,5) - 4*pow(x,4) + 3*pow(x,3) + 2*pow(x,2) - 7*x + 10

def methode_secante(function,x0,x1,tol,max_iter):
    iter = 0
    while abs(function(x1))>tol and iter<max_iter:
        if function(x1)-function(x0):
            temp = x1
            x1 = x0 - function(x0)*(x1-x0)/(function(x1)-function(x0))
            x0 = temp
            iter += 1
        else: 
            x1 += 1
    return x1

def error(function,x0,x1,tol,max_iter,correct_value):
    distances = []
    iter = 0
    while abs(function(x1))>tol and iter<max_iter:
        if function(x1)-function(x0):
            distances.append(abs(x1-correct_value))
            temp = x1
            x1 = x0 - function(x0)*(x1-x0)/(function(x1)-function(x0))
            x0 = temp
            iter += 1
        else:
            x1 += 1
    distances.append(abs(x1-correct_value))

    plt.plot(distances,marker = ".")
    plt.xlabel("Iteration")
    plt.ylabel("distance from the correct value")
    plt.title("convergence of the secante method")
    plt.show()

print(methode_secante(f1,0,50,10**(-4),10**(4)))
print(methode_secante(f2,0,50,10**(-4),10**(4)))
print(methode_secante(f3,0,50,10**(-4),10**(4)))
print(methode_secante(f4,0,50,10**(-4),10**(4)))
