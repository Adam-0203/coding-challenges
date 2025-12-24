# Dichotomy (Bisection) Method

## Description
This module implements the **Dichotomy (Bisection) method** to find a numerical solution of a nonlinear equation:

f(x) = 0

The method is based on repeatedly dividing an interval where the function changes sign.

---

## Method Principle
Given a continuous function `f` on `[a, b]` such that:

f(a) · f(b) < 0

There exists at least one root in the interval.

At each iteration:
- Compute the midpoint `m = (a + b) / 2`
- Keep the subinterval where the sign change occurs
- Stop when the interval size is smaller than the tolerance

---

## Convergence
- **Convergence type:** Linear
- **Reliability:** Guaranteed if the sign condition is satisfied
- **Speed:** Slow compared to Newton or Secant methods

---

## Implemented Functions
The code includes several test functions:
- Polynomial functions
- Trigonometric function
- Exponential function

These functions are used to test robustness and convergence behavior.

---

## Main Functions

### `dichotomie(f, a, b, tol)`
Computes an approximation of a root of `f` in the interval `[a, b]`.

**Parameters**
- `f`: function to solve  
- `a`, `b`: interval bounds  
- `tol`: tolerance  

**Returns**
- Approximate root

---

### `error(f, a, b, tol, max_iter, correct_value)`
Plots the distance between the numerical approximation and the exact root at each iteration.

Used to visualize convergence.

---

## Example
```python
dichotomie(function, 1, 2, 1e-8)
