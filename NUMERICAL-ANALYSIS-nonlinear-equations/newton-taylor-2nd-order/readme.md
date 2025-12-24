# Newton Method with Second-Order Taylor Approximation

## Description
This module implements a **variation of Newton’s method** based on a **second-order Taylor expansion** of the function.

The method improves the classical Newton approach by incorporating the **second derivative** to refine the update step.

---

## Principle
The function f(x) is locally approximated using its **second-order Taylor expansion** around the current point xₙ.

Instead of using a linear approximation (tangent), the method solves a **quadratic approximation** of f(x) to compute the next iterate.

This leads to the update rule derived from:
- f(x)
- f′(x)
- f″(x)

---

## Iteration Formula
At each step, the next approximation is computed by solving the quadratic equation:

f′(xₙ)² − 2 f″(xₙ) f(xₙ) ≥ 0

If the condition is satisfied, the update is:

xₙ₊₁ = xₙ + [ −f′(xₙ) − √( f′(xₙ)² − 2 f″(xₙ) f(xₙ) ) ] / f″(xₙ)

If not, a small correction is applied to continue the iteration.

---

## Convergence
- **Convergence type:** Faster than classical Newton in favorable cases
- **Behavior:** More aggressive update
- **Cost:** Higher per iteration due to second derivative

---

## Requirements
- f must be twice differentiable
- f′(x) and f″(x) must be available
- Discriminant must be non-negative

---

## Main Function

### `newton_second(f, f_prime, f_second, x0, tol)`
Computes an approximation of a root using second-order information.

**Parameters**
- `f`: function  
- `f_prime`: first derivative  
- `f_second`: second derivative  
- `x0`: initial guess  
- `tol`: stopping tolerance  

**Returns**
- Approximate root

---

## Example
```python
newton_second(g, g_prime, g_second, 10, 1e-8)
