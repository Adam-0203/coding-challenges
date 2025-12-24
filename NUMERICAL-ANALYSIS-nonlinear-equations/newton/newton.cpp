#include <iostream>
#include <cmath>
#include <functional>

// double f(double x){
//     return pow(x,3) -x +1;
// }

// double f_prime(double x){
//     return 3*pow(x,2) - 1;
// }

double f(double x){
    return pow(x,2) -2;
}

double f_prime(double x){
    return 2*x;
}

double methode(std::function<double(double)> function, std::function<double(double)> derived, 
              double point, double precision,double max_iter){

    int iter = 0;

    while ((std::abs(function(point)) > precision) && (iter<max_iter)){
        point = point - (function(point)/derived(point));
        iter++;
    }

    return point;
}

int main(){
    std::cout << methode(f,f_prime,-10000,pow(10,-12),pow(10,12)) << std::endl;
}
