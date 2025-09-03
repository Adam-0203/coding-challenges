#include "Savings_Account.h"

Savings_Account::Savings_Account(std::string name, double balance, double int_rate)
    : Account(name, balance), int_rate(int_rate) {}

bool Savings_Account::deposit(double amount){
    if (amount>0){
        balance += amount*(1+int_rate/100);
        return true;
    }
    return false;
}

ostream& operator<<(ostream& os, const Savings_Account& acc){
    os << "[Savings Account:  " << acc.name << " : " << acc.balance << " "<< acc.int_rate<< " ]";
    return os;
}