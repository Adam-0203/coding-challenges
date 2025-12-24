import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import exp
distances1 = []
distances2 = []
distances3 = []

#the functions we will be using
def f1(x):
    return x*x*x - x + 1
def f1_prime(x):
    return 3*x*x - 1

def g(x):
    return x*x - 2
def g_prime(x):
    return 2*x

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

#the newton method
def newton(point,function,derived,precision,max_iter):
    iter = 0
    while function(point) > precision and iter<max_iter:
        point = point - function(point)/derived(point)
        iter += 1

    return point

def error_newton(point,function,derived,precision, max_iter,correct_value):
    iter = 0
    while function(point) > precision and iter<max_iter:
        distances1.append(abs(point-correct_value))
        point = point - function(point)/derived(point)
        iter += 1
    distances1.append(abs(point-correct_value))

#the secante method
def secante(function,x0,x1,tol,max_iter):
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

def error_secante(function,x0,x1,tol,max_iter,correct_value):
    iter = 0
    while abs(function(x1))>tol and iter<max_iter:
        if function(x1)-function(x0):
            distances2.append(abs(x1-correct_value))
            temp = x1
            x1 = x0 - function(x0)*(x1-x0)/(function(x1)-function(x0))
            x0 = temp
            iter += 1
        else:
            x1 += 1
    distances2.append(abs(x1-correct_value))

#the dichotomie method
def dichotomie(f,a,b,tol,max_iter):

    iter = 0
    
    mid = (a+b)/2
    while abs(b-a)>tol and max_iter>iter:
        mid = (a+b)/2
        if f(mid) == 0:
            return mid
        if f(a)*f(mid)<0:
            b = mid
        elif f(b)*f(mid)<0:
            a = mid
        iter += 1
    return mid

def error_dichotomie(f,a,b,tol,max_iter,correct_value):
    iter = 0

    mid = (a+b)/2
    while abs(b-a)>tol and max_iter>iter and f(mid):
        mid = (a+b)/2
        distances3.append(abs(mid-correct_value))
        if f(a)*f(mid)<0:
            b = mid
        elif f(b)*f(mid)<0:
            a = mid
        iter += 1
    distances3.append(abs(mid-correct_value))

def comparaison(function,derived,x0,x1,a,b,point,tol,max_iter):
    correct_value1 = newton(point,function,derived,tol, max_iter)
    correct_value2 = secante(function,x0,x1,tol,max_iter) 
    correct_value3 = dichotomie(function,a,b,tol,max_iter)
    # print(correct_value1,correct_value2,correct_value3)

    error_newton(point,function,derived,tol, max_iter,correct_value1)
    error_secante(function,x0,x1,tol,max_iter,correct_value2)
    error_dichotomie(function,a,b,tol,max_iter,correct_value3)

    plt.plot(distances1,label="newton")
    plt.plot(distances2,label="secante")
    plt.plot(distances3,label="dichotomie")
    plt.xlabel("iteration")
    plt.ylabel("distance from the correct value")
    plt.title("difference in convergence between the methods")
    plt.legend()
    plt.show()

comparaison(f1,f1_prime,10,12,0.5,10,10,10**(-4),50)
