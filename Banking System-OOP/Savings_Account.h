#ifndef S_ACCOUNT
#define S_ACCOUNT

#include "Account.h"
#include <iostream>

class Savings_Account : public Account
{
    private:
        static constexpr double def_int_rate= 0.0;
    public:
        double int_rate;
        bool deposit(double amount);
        Savings_Account(std::string name ="unNamed" , double balance = 0.0, double int_rate = def_int_rate);
        friend ostream& operator<<(ostream& os, const Savings_Account& acc);
};


#endif