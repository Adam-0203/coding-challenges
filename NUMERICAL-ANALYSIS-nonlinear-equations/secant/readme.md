# Secant Method

## Description
This module implements the **Secant method** to solve nonlinear equations of the form:

f(x) = 0

The Secant method is an **iterative root-finding algorithm** that approximates the derivative using two previous points, avoiding explicit differentiation.

---

## Principle
Starting from two initial guesses \( x_0 \) and \( x_1 \), the method builds a sequence using the secant line:

xₙ₊₁ = xₙ − f(xₙ) · (xₙ − xₙ₋₁) / ( f(xₙ) − f(xₙ₋₁) )

At each iteration, the intersection of the secant line with the x-axis provides the next approximation.

---

## Convergence
- **Convergence type:** Superlinear
- **Speed:** Faster than dichotomy, slower than Newton
- **Behavior:** Efficient when derivatives are unavailable

---

## Requirements
- Two initial approximations
- f must be continuous near the root
- f(xₙ) ≠ f(xₙ₋₁) to avoid division by zero

---

## Implemented Functions
The method is tested on:
- Polynomial functions
- Trigonometric functions
- Exponential functions

This allows comparison across different function behaviors.

---

## Main Functions

### `methode_secante(function, x0, x1, tol, max_iter)`
Computes an approximation of a root using two initial points.

**Parameters**
- `function`: f(x)  
- `x0`, `x1`: initial guesses  
- `tol`: stopping tolerance  
- `max_iter`: maximum iterations  

**Returns**
- Approximate root

---

### `error(function, x0, x1, tol, max_iter, correct_value)`
Plots the distance between the numerical approximation and the exact root at each iteration.

Used to analyze convergence behavior.

---

## Example
```python
methode_secante(f1, 0, 50, 1e-4, 10000)
