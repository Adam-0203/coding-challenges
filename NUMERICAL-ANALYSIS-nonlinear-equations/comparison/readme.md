# Comparison of Root-Finding Methods

## Description
This module compares the **convergence behavior** of three classical methods used to solve nonlinear equations:

- Dichotomy (Bisection)
- Newton’s method
- Secant method

The comparison focuses on **efficiency and convergence speed**.

---

## Objective
The goal is to observe how fast each method converges to a root by tracking the **distance to the final solution** at each iteration.

All methods are applied to the **same function** and under comparable conditions.

---

## Compared Methods

### Dichotomy
- Guaranteed convergence
- Linear convergence
- Slow but very stable

### Newton
- Uses first derivative
- Quadratic convergence
- Fast near the root

### Secant
- No derivative required
- Superlinear convergence
- Faster than dichotomy, less stable than Newton

---

## Comparison Strategy
1. Compute a reference root using each method
2. Measure the distance between each iteration and the final value
3. Plot the distances versus the number of iterations
4. Display all curves on the same graph

This allows a **direct visual comparison** of convergence speed.

---

## Metrics Used
- Number of iterations
- Distance from the final solution
- Convergence rate (visual)

Execution time is not considered.

---

## Visualization
The plot shows:
- X-axis: iteration number
- Y-axis: distance from the final value
- One curve per method

A steeper curve indicates faster convergence.

---

## Example
```python
comparaison(f1, f1_prime, 10, 12, 0.5, 10, 10, 1e-4, 50)
