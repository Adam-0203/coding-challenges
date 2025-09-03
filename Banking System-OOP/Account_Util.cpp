// Account_Util.cpp
#include "Account_Util.h"
#include <iostream>

void display(const std::vector<Account>& accounts) {
    for (const auto& account : accounts) {
        std::cout << account << std::endl;
    }
    std::cout << endl;
}

void display(const std::vector<Savings_Account>& accounts) {
    for (const auto& account : accounts) {
        std::cout << account << std::endl;
    }
    std::cout << endl;
}

void display(const std::vector<Checking_Account>& accounts) {
    for (const auto& account : accounts) {
        std::cout << account << std::endl;
    }
    std::cout << endl;
}

void display(const std::vector<Trust_Account>& accounts) {
    for (const auto& account : accounts) {
        std::cout << account << std::endl;
    }
    std::cout << endl;
}

// Deposit functions
void deposit(std::vector<Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.deposit(amount);
    }
}

void deposit(std::vector<Savings_Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.deposit(amount);
    }
}

void deposit(std::vector<Checking_Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.deposit(amount);
    }
}

void deposit(std::vector<Trust_Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.deposit(amount);
    }
}

// Withdraw functions
void withdraw(std::vector<Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.withdraw(amount);
    }
}

void withdraw(std::vector<Savings_Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.withdraw(amount);
    }
}

void withdraw(std::vector<Checking_Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.withdraw(amount);
    }
}

void withdraw(std::vector<Trust_Account>& accounts, double amount) {
    for (auto& account : accounts) {
        account.withdraw(amount);
    }
}
