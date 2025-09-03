# Run-Length Encoding (RLE) in C++

This C++ project implements a **simple Run-Length Encoding (RLE)** algorithm to compress strings by replacing consecutive repeated characters with the character followed by its count.

## How it Works

- The function `encode_rle` takes a string and compresses it:
  - It counts consecutive occurrences of each character.
  - It appends the character followed by its count to the result string.
  
Example:
```text
Input:  aaaabbbcc
Output: a4b3c2

## Limitation with Digits

⚠️ **Important:** This version **does not handle digits in the input correctly**.  

**Example:**
```text
Input:  a11b
Output: a112b
