#include <iostream>
#include <functional>
#include <cmath>
#include <tuple>

double f(double x){
    return pow(x,2) -2;
}

auto methode_secante(std::function<double(double)> function,double x0, double x1, double tol, double max_iter){
    double iter = 0;
    while (fabs(function(x1))>tol){
        double temp = x1;
        iter++;

        x1 = x0 - ((x0-x1)/(function(x0)-function(x1)))*function(x0);
        x0 = temp;
    }
    return std::make_tuple(x1,x0);
}

int main(){
    auto t = methode_secante(f,-6,600,pow(10,-8),pow(10,4));
    auto one = std::get<0>(t);
    auto second = std::get<0>(t);
    std::cout << one << " and " << second << std::endl;
    return 0;
}
