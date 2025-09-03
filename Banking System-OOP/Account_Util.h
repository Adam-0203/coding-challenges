// Account_Util.h
#include <vector>
#include "Account.h"
#include "Savings_Account.h"
#include "Checking_Account.h"
#include "Trust_Account.h"

// Function to display accounts
void display(const std::vector<Account>& accounts);
void display(const std::vector<Savings_Account>& accounts);
void display(const std::vector<Checking_Account>& accounts);
void display(const std::vector<Trust_Account>& accounts);

// Function to deposit money
void deposit(std::vector<Account>& accounts, double amount);
void deposit(std::vector<Savings_Account>& accounts, double amount);
void deposit(std::vector<Checking_Account>& accounts, double amount);
void deposit(std::vector<Trust_Account>& accounts, double amount);

// Function to withdraw money
void withdraw(std::vector<Account>& accounts, double amount);
void withdraw(std::vector<Savings_Account>& accounts, double amount);
void withdraw(std::vector<Checking_Account>& accounts, double amount);
void withdraw(std::vector<Trust_Account>& accounts, double amount);
