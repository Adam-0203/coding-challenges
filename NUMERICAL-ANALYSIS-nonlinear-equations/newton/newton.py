import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import exp

def f1(x):
    return x*x*x - x + 1
def f1_prime(x):
    return 3*x*x - 1

def f2(x):
    return sin(x) - 0.5
def f2_prime(x):
    return  cos(x)

def f3(x):
    return exp(x) - 2
def f3_prime(x):
    return exp(x)

def f4(x):
    return pow(x,5) - 4*pow(x,4) + 3*pow(x,3) + 2*pow(x,2) - 7*x + 10
def f4_prime(x):
    return 5*pow(x,4) - 16*pow(x,3) + 9*pow(x,2) + 4*x - 7

def newton(point,function,derived,precision,max_iter):
    iter = 0
    while function(point) > precision and iter<max_iter:
        point = point - function(point)/derived(point)
        iter += 1

    return point

def error(point,function,derived,precision, max_iter,correct_value):
    iter = 0
    distances = []
    while function(point) > precision and iter<max_iter:
        distances.append(abs(point-correct_value))
        point = point - function(point)/derived(point)
        iter += 1
    distances.append(abs(point-correct_value))
    
    print(point)
    plt.plot(distances, marker='.')
    plt.xlabel("Iteration")
    plt.ylabel("Distance from correct value")
    plt.title("Convergence of Newton's method")
    plt.show()


valeur1 = newton(-1,f1,f1_prime,10**(-4),10**4)
valeur2 = newton(1081,f2,f2_prime,10**(-4),10**4)
valeur3 = newton(1,f3,f3_prime,10**(-4),10**4)
valeur4 = newton(1,f4,f4_prime,10**(-4),10**4)
print(valeur1,valeur2,valeur3,valeur4)
