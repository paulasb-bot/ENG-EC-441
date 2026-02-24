# CRC Error Control – Mathematical Analysis and Implementation

## 1. Introduction

In the Data Link layer, error detection mechanisms are essential to ensure that corrupted frames are not accepted as valid. One of the most powerful error detection techniques is the Cyclic Redundancy Check (CRC).

Unlike simple parity bits, CRC treats a bit string as a polynomial over GF(2) and performs polynomial division using modulo-2 arithmetic (where subtraction is equivalent to XOR). The remainder of this division is appended to the transmitted data.

At the receiver, the same division is performed. If the remainder is non-zero, an error is detected.

---

## 2. Problem Statement

Given the data:

Data: 1101011011  

Generator polynomial:

G = 10011  

Tasks:

1. Compute the CRC manually.  
2. Determine the transmitted frame.  
3. Implement CRC in Python.  
4. Simulate a transmission error and verify that it is detected.  

---

## 3. Manual CRC Computation

The generator has 5 bits, so its degree is 4.

Therefore, we append 4 zeros to the original data:

1101011011 0000

Now we perform modulo-2 division:

11010110110000 ÷ 10011

In modulo-2 arithmetic:

- There is no borrowing.
- Subtraction is equivalent to XOR.
- We only perform division when the leftmost bit is 1.
- Each subtraction step is replaced by a bitwise XOR.

After completing the XOR long division, the remainder obtained is:

1110

---

## 4. Transmitted Frame

The CRC bits are the remainder:

CRC = 1110

The transmitted frame becomes:

1101011011 1110

This transmitted bit string is divisible by the generator polynomial:

T(x) mod G(x) = 0

---

## 5. Python Implementation

To verify the manual result and simulate error detection, we implement CRC in Python.

```python
def crc_remainder(data: str, generator: str) -> str:
    padded_data = list(data + '0' * (len(generator) - 1))
    generator = list(generator)

    for i in range(len(data)):
        if padded_data[i] == '1':
            for j in range(len(generator)):
                padded_data[i + j] = str(
                    int(padded_data[i + j] != generator[j])
                )

    remainder = ''.join(padded_data[-(len(generator) - 1):])
    return remainder


def verify_crc(frame: str, generator: str) -> str:
    padded_data = list(frame)
    generator = list(generator)

    for i in range(len(frame) - len(generator) + 1):
        if padded_data[i] == '1':
            for j in range(len(generator)):
                padded_data[i + j] = str(
                    int(padded_data[i + j] != generator[j])
                )

    remainder = ''.join(padded_data[-(len(generator) - 1):])
    return remainder


if __name__ == "__main__":
    data = "1101011011"
    generator = "10011"

    remainder = crc_remainder(data, generator)
    transmitted = data + remainder

    print("CRC:", remainder)
    print("Transmitted frame:", transmitted)

    # Introduce single-bit error
    error_frame = list(transmitted)
    error_frame[5] = '1' if error_frame[5] == '0' else '0'
    error_frame = ''.join(error_frame)

    print("Error frame:", error_frame)
    print("Verification remainder:", verify_crc(error_frame, generator))
```

---

## 6. Code Explanation

The function `crc_remainder`:

- Appends zeros equal to the degree of the generator polynomial.
- Iterates through the data bits.
- Applies XOR using logical inequality (`!=`) to simulate modulo-2 subtraction.
- Returns the final remainder.

In GF(2), addition and subtraction are equivalent to XOR. This is why logical inequality is used to simulate bitwise XOR operations in Python.

The `verify_crc` function performs the same division on the received frame. If the remainder is not all zeros, an error has occurred.

---

## 7. Error Detection Experiment

A single-bit error was introduced into the transmitted frame by flipping one bit.

When the corrupted frame is divided again by the generator polynomial, the remainder is non-zero.

This confirms that CRC detects all single-bit errors.

Mathematically, a single-bit error corresponds to a polynomial of the form x^k. If the generator polynomial has at least two non-zero terms, it cannot divide x^k, so the remainder cannot be zero.

---

## 8. Error Detection Capabilities

CRC detects:

- All single-bit errors
- All burst errors of length less than or equal to r (where r is the degree of the generator polynomial)
- Most longer burst errors

However, CRC does not detect all possible error patterns. Its effectiveness depends on the chosen generator polynomial.

In practical systems such as Ethernet, carefully selected generator polynomials provide very strong error detection guarantees.

---

## 9. Reflection

This exercise demonstrates how polynomial arithmetic in GF(2) directly applies to real networking systems.

CRC provides significantly stronger protection than simple parity bits while introducing minimal overhead. It is widely used in the Data Link layer to ensure reliable frame transmission.

Combining manual derivation with programmatic implementation reinforced both the mathematical foundation and the practical behavior of CRC.