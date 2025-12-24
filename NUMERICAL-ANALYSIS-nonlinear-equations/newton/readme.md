# Newton's Method

## Description
This module implements **Newton's method** to numerically solve nonlinear equations of the form:

f(x) = 0

It is an **iterative method** that uses the function and its derivative to rapidly converge to a root.

---

## Principle
Starting from an initial guess \( x_0 \), Newton’s method builds a sequence:

xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)

Each iteration replaces the function by its **tangent line** and computes where this tangent intersects the x-axis.

---

## Convergence
- **Convergence type:** Quadratic ⚡
- **Speed:** Very fast near the root
- **Condition:** Requires a good initial guess

---

## Requirements
For Newton’s method to work properly:
- f must be differentiable
- f′(x) must not be zero at the solution
- The initial point should be close to the root

---

## Implemented Functions
The code tests Newton’s method on:
- Polynomial functions
- Trigonometric functions
- Exponential functions

Each function is paired with its analytical derivative.

---

## Main Functions

### `newton(point, function, derived, precision, max_iter)`
Computes an approximation of a root starting from an initial point.

**Parameters**
- `point`: initial guess  
- `function`: f(x)  
- `derived`: f′(x)  
- `precision`: stopping tolerance  
- `max_iter`: maximum iterations  

**Returns**
- Approximate root

---

### `error(point, function, derived, precision, max_iter, correct_value)`
Plots the distance between the current approximation and the exact root at each iteration.

Used to observe **quadratic convergence**.

---

## Example
```python
newton(1, f3, f3_prime, 1e-4, 10000)
