#include "Trust_Account.h"

Trust_Account::Trust_Account(std::string name, double balance, double int_rate) : Savings_Account(name,balance,int_rate){};

bool Trust_Account::deposit(double amount){
    if (amount>0){
        balance += amount*(1+int_rate/100);
        if (amount >= bonus_threshold){
            balance += bonus_amount;
        }
        return true;
    }
    return false;
}


bool Trust_Account::withdraw(double amount){
    if (num_withdrawals >= max_withdrawals){
        return false;
    }
    else if (balance - amount < 0){
        return false;
    }
    else if (amount > balance*max_withdraw_percent){
        return false;
    }
    else{
        balance -= amount;
        num_withdrawals += 1;
        return true;
    }
}

std::ostream& operator<<(std::ostream& os,const Trust_Account& acc){
    os << "[Trust Account:  " << acc.name << " : " << acc.balance << " "<< acc.int_rate<< " : " << acc.num_withdrawals <<" ]";
    return os;
}