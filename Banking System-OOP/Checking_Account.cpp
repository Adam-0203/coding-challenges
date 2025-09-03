#include "Checking_Account.h"

Checking_Account::Checking_Account(std::string name, double balance) : Account(name, balance) {}

std::ostream& operator<<(std::ostream& os,const Checking_Account& acc){
    os << "[Checking Account :  " << acc.name << " : " << acc.balance << " ]";
    return os;
}

bool Checking_Account::withdraw(double amount){
    if (balance -amount - per_check_fee >= 0){
        balance = balance -amount - per_check_fee;
        return true;
    }
    return false;
}