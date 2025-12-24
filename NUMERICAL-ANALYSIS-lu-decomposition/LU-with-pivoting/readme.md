# LU Decomposition (With Partial Pivoting)

## Description
This module implements the **LU decomposition with partial pivoting** for a square matrix:

P · A = L · U

where:
- **P** is a permutation matrix  
- **L** is a lower triangular matrix with ones on the diagonal  
- **U** is an upper triangular matrix  

Pivoting improves numerical stability compared to the standard LU decomposition.

---

## Method Principle
Partial pivoting ensures that the **largest available element in the current column** is used as the pivot at each elimination step.

At each iteration:
1. Find the row with the largest absolute value in the current column
2. Swap rows in A and update the permutation matrix P
3. Apply Gaussian elimination using elementary matrices M_i
4. Accumulate multipliers into L

The decomposition satisfies:

P · A ≈ L · U

---

## Algorithm Steps
1. Generate a random square matrix A  
2. Initialize L and permutation matrix P as identity matrices  
3. For each column:
   - Identify the pivot row
   - Swap rows in A and P
   - Swap corresponding rows in L for previous columns
   - Apply elimination and update L
4. U is obtained after elimination
5. Verify decomposition: P · A ≈ L · U

---

## Main Functions

### `M(i, A)`
Constructs the elementary elimination matrix for step `i` and updates L.

---

### `permuter_L(i, j, k)`
Swaps rows in L to maintain correctness after pivoting.

---

### `LU_factor(A)`
Performs LU factorization with partial pivoting.

**Returns**
- `L`: lower triangular matrix  
- `U`: upper triangular matrix  

---

## Verification
Check correctness by comparing:

P · A ≈ L · U

Matrix multiplication results should match up to numerical precision.

---

## Notes
- Pivoting ensures stability and avoids division by small numbers  
- Essential for matrices where zero or small pivot elements may appear  
- Implementation is educational and done **from scratch**

---

## Context
This method is part of a **numerical analysis study** exploring matrix factorization techniques and their robustness.
