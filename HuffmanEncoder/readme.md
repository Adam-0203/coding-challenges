# Huffman Encoding Project

## Description
This project implements **Huffman encoding**, a **lossless data compression algorithm** that assigns variable-length codes to input characters based on their frequencies.  

The goal is to compress text data efficiently and then decode it back to its original form without losing any information. This project demonstrates the practical implementation of **tree-based encoding** and binary operations in Java.

---

## Features
- Build a **Huffman tree** from input text based on character frequencies  
- Generate **variable-length codes** for each character  
- Encode text into a **compressed binary representation**  
- Decode compressed data back to the **original text**  
- **Visualization of the Huffman tree and codes** (in progress)  
- Unit-tested components to ensure **correctness and reliability**  

---

## How It Works
1. **Frequency Analysis**: Count the number of occurrences of each character in the input text.  
2. **Tree Construction**: Build a **binary Huffman tree** where each leaf node represents a character. Characters with higher frequencies are closer to the root.  
3. **Code Assignment**: Traverse the tree to assign **unique binary codes** to each character.  
4. **Encoding**: Replace each character in the input text with its corresponding binary code to generate compressed data.  
5. **Decoding**: Read the binary stream and traverse the Huffman tree to reconstruct the original text.
