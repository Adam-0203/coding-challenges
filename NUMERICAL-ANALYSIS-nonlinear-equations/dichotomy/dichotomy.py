import matplotlib.pyplot as plt
from math import sin,exp

def function(x):
    return x*x - 2

def f1(x):
    return x*x*x - x + 1

def f2(x):
    return sin(x) - 0.5

def f3(x):
    return exp(x) - 2

def f4(x):
    return pow(x,5) - 4*pow(x,4) + 3*pow(x,3) + 2*pow(x,2) - 7*x + 10

def dichotomie(f,a,b,tol):

    iter = 0
    while abs(b-a)>tol:
        mid = (a+b)/2
        if f(mid) == 0:
            return mid
        if f(a)*f(mid)<0:
            b = mid
        elif f(a)*f(mid)>0:
            a = mid
        iter += 1
    return mid


def error(f,a,b,tol,max_iter,correct_value):
    distances = []
    iter = 0
    mid = (a+b)/2
    while abs(b-a)>tol and max_iter>iter and f(mid):
        mid = (a+b)/2
        distances.append(abs(mid-correct_value))
        if f(a)*f(mid)<0:
            b = mid
        elif f(b)*f(mid)<0:
            a = mid
        iter += 1
    distances.append(abs(mid-correct_value))

    distances.append(abs(mid-correct_value))
    plt.plot(distances,marker=".")
    plt.xlabel("iteration")
    plt.xlabel("distance from the correct value")
    plt.title("convergence of the dichotomie method")
    plt.show()



# error(f1,-100,54,10**(-4),10**(4),dichotomie(f1,-100,54,10**(-4),10**(4)))
# error(f2,-100,54,10**(-4),10**(4),dichotomie(f2,-100,54,10**(-4),10**(4)))
# error(f3,-100,54,10**(-4),10**(4),dichotomie(f3,-100,54,10**(-4),10**(4)))
# error(f4,-100,54,10**(-4),10**(4),dichotomie(f4,-100,54,10**(-4),10**(4)))


print(dichotomie(function,1,2,(10**(-8))))
