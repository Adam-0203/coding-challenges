#ifndef C_ACCOUNT
#define C_ACCOUNT

#include "Account.h"

class Checking_Account : public Account
{
    private:
        static constexpr double per_check_fee = 1.5;

    public:
        Checking_Account(std::string name = "unNamed", double balance = 0.0);
        bool withdraw(double amount);
        friend std::ostream& operator<<(ostream& os,const Checking_Account& acc);
};

#endif