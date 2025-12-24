# LU Decomposition (Without Pivoting)

## Description
This module implements the **LU decomposition without pivoting** for a square matrix:

A = L · U

where:
- **L** is a lower triangular matrix with ones on the diagonal  
- **U** is an upper triangular matrix  

The implementation is done **from scratch**, without using built-in LU routines.

---

## Method Principle
The algorithm is based on **Gaussian elimination**.

At each step:
- An elementary matrix \( M_i \) is constructed
- The matrix A is transformed progressively into an upper triangular matrix U
- The multipliers used during elimination are stored in L

The decomposition satisfies:
A ≈ L · U

---

## Algorithm Steps
1. Generate a random square matrix A
2. Initialize L as the identity matrix
3. Apply successive elimination matrices \( M_i \)
4. Accumulate coefficients into L
5. Obtain U after elimination
6. Verify the decomposition by computing ‖A − LU‖

---

## Main Functions

### `M(i, A)`
Constructs the elementary elimination matrix used at step `i`.

Also updates the corresponding coefficients in matrix **L**.

---

### `LU_factor(A)`
Performs the LU factorization of matrix `A`.

**Returns**
- `L`: lower triangular matrix  
- `U`: upper triangular matrix  

---

## Verification
The accuracy of the decomposition is verified by computing:

‖ A − L·U ‖₁

A small value confirms the correctness of the factorization.

---

## Notes
- No row permutations are used
- The method may fail if a pivot element is zero
- This implementation is intended for **educational purposes**

---

## Context
This implementation is part of a **numerical analysis project** focused on matrix factorization techniques and their properties.
