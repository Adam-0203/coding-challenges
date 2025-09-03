#ifndef ACCOUNT
#define ACCOUNT

#include <iostream>
#include <string>
using namespace std;

class Account
{
    private:
        static constexpr const char* def_name = "unNamed"; 
        static constexpr double def_balance = 0.0; 

    protected:
        string name;
        double balance;

    public:
        bool deposit(double amount);
        bool withdraw(double amount);
        friend ostream& operator<<(ostream& os, const Account& acc);
        Account(std::string name = def_name, double balance = def_balance);

};

#endif