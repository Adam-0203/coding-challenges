# C++ Banking System Simulation

A C++ console application that demonstrates core Object-Oriented Programming (OOP) principles by simulating a simple banking system with multiple account types.

## Overview

This project models a banking system with a hierarchy of account classes, each with specific rules for deposits and withdrawals. It serves as a practical example of inheritance, polymorphism, and encapsulation in C++.

## Account Types

*   **Account:** The base class with standard deposit/withdraw functionality.
*   **Savings_Account:** Inherits from `Account` and adds an interest rate on deposits.
*   **Checking_Account:** Inherits from `Account` and deducts a fee for every withdrawal.
*   **Trust_Account:** Inherits from `Savings_Account` and adds rules for limited withdrawals, bonuses on large deposits, and a maximum withdrawal percentage.

## Key Features

*   **Class Hierarchy:** Demonstrates inheritance (`is-a` relationships).
*   **Polymorphism:** Uses overloaded functions to handle different account types.
*   **Encapsulation:** Keeps member data protected and exposes public interfaces.
*   **Static Members:** Utilizes `static constexpr` for class-wide constants.

## How to Build and Run

1.  **Compile:** Ensure all `.cpp` files are compiled and linked together.
    ```bash
    g++ -std=c++11 *.cpp -o banking_system
    ```
2.  **Run:**
    ```bash
    ./banking_system
    ```

## Sample Output

The program will create vectors of each account type, perform a series of deposits and withdrawals, and display the state of all accounts after each operation, showcasing the unique behavior of each account type.
