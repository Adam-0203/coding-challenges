#include "Account.h"

Account::Account(string name,double balance)
{
    this->name = name;
    this->balance = balance;
}

bool Account::deposit(double amount){
    if (amount >0){
        balance += amount;
        return true;
    }
    return false;
}


bool Account::withdraw(double amount){
    if (amount>0 && (balance-amount)>=0){
        balance -= amount;
        return true;
    }
    return false;
}

ostream& operator<<(ostream& os, const Account& acc){
    os << "[Account:  " << acc.name << " : " << acc.balance << " ]";
    return os;
}