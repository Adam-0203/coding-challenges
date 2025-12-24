# Dichotomy (Bisection) Method

## Overview
This project implements the **Dichotomy method** (also called the **Bisection method**) to solve **nonlinear equations of the form**:

\[
f(x) = 0
\]

It is a **robust and reliable** root-finding method based on interval subdivision.

---

## Principle of the Method
Given a continuous function \( f \) on an interval \([a, b]\) such that:

\[
f(a) \cdot f(b) < 0
\]

there exists **at least one root** in the interval (Intermediate Value Theorem).

The method:
1. Computes the midpoint \( m = \frac{a+b}{2} \)
2. Selects the subinterval where the sign change occurs
3. Repeats until the desired tolerance is reached

---

## Convergence
- **Type:** Linear convergence 📉
- **Guaranteed convergence** if assumptions are satisfied
- **Slow** compared to Newton or Secant methods, but very stable

---

## Implemented Functions

Several test functions are included:
- Polynomial functions
- Trigonometric function
- Exponential function

Examples:
```python
x^2 - 2
x^3 - x + 1
sin(x) - 0.5
exp(x) - 2
# Dichotomy (Bisection) Method

## Overview
This project implements the **Dichotomy method** (also called the **Bisection method**) to solve **nonlinear equations of the form**:

\[
f(x) = 0
\]

It is a **robust and reliable** root-finding method based on interval subdivision.

---

## Principle of the Method
Given a continuous function \( f \) on an interval \([a, b]\) such that:

\[
f(a) \cdot f(b) < 0
\]

there exists **at least one root** in the interval (Intermediate Value Theorem).

The method:
1. Computes the midpoint \( m = \frac{a+b}{2} \)
2. Selects the subinterval where the sign change occurs
3. Repeats until the desired tolerance is reached

---

## Convergence
- **Type:** Linear convergence 📉
- **Guaranteed convergence** if assumptions are satisfied
- **Slow** compared to Newton or Secant methods, but very stable

---

## Implemented Functions

Several test functions are included:
- Polynomial functions
- Trigonometric function
- Exponential function

Examples:
```python
x^2 - 2
x^3 - x + 1
sin(x) - 0.5
exp(x) - 2
