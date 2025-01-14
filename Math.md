# Math Cheat Sheet for Coding

## Arithmetic Operations
| Operation        | Symbol   | Example        | Output |
|------------------|----------|----------------|--------|
| Addition         | `+`      | `5 + 3`        | `8`    |
| Subtraction      | `-`      | `5 - 3`        | `2`    |
| Multiplication   | `*`      | `5 * 3`        | `15`   |
| Division         | `/`      | `5 / 3`        | `1.6667` |
| Floor Division   | `//`     | `5 // 3`       | `1`    |
| Modulus          | `%`      | `5 % 3`        | `2`    |
| Exponentiation   | `**`     | `5 ** 3`       | `125`  |

---

## Order of Operations
Use **PEMDAS**:
1. Parentheses `()`
2. Exponents `**`
3. Multiplication `*` and Division `/` or `//`
4. Addition `+` and Subtraction `-`

Example:
```python
result = (5 + 3) * 2 ** 2
# Output: 32
```

---

## Common Mathematical Functions
| Function        | Description           | Example                  | Output |
|------------------|-----------------------|--------------------------|--------|
| `abs(x)`         | Absolute value        | `abs(-5)`                | `5`    |
| `round(x, n)`    | Rounds to `n` decimals | `round(3.14159, 2)`      | `3.14` |
| `max(a, b, ...)` | Maximum value         | `max(1, 5, 3)`           | `5`    |
| `min(a, b, ...)` | Minimum value         | `min(1, 5, 3)`           | `1`    |
| `sum(iterable)`  | Sum of elements       | `sum([1, 2, 3])`         | `6`    |

---

## Importing Math Library
For advanced math functions, use Python's `math` module:
```python
import math
```

### Math Constants
| Constant         | Description           | Example         |
|------------------|-----------------------|-----------------|
| `math.pi`        | Value of π            | `3.141592653589793` |
| `math.e`         | Base of natural log   | `2.718281828459045` |

### Math Functions
| Function                  | Description                       | Example                     | Output         |
|---------------------------|-----------------------------------|-----------------------------|----------------|
| `math.sqrt(x)`            | Square root                      | `math.sqrt(25)`            | `5.0`          |
| `math.pow(x, y)`          | x raised to power y              | `math.pow(2, 3)`           | `8.0`          |
| `math.log(x)`             | Natural log                      | `math.log(math.e)`         | `1.0`          |
| `math.log10(x)`           | Logarithm base 10                | `math.log10(100)`          | `2.0`          |
| `math.ceil(x)`            | Ceiling value                    | `math.ceil(3.4)`           | `4`            |
| `math.floor(x)`           | Floor value                      | `math.floor(3.4)`          | `3`            |
| `math.sin(x)`             | Sine of x (radians)              | `math.sin(math.pi / 2)`    | `1.0`          |
| `math.cos(x)`             | Cosine of x (radians)            | `math.cos(math.pi)`        | `-1.0`         |
| `math.factorial(x)`       | Factorial of x                   | `math.factorial(5)`        | `120`          |

---

## Random Numbers
Use Python's `random` module for generating random numbers:
```python
import random
```

| Function                  | Description                       | Example                     | Output               |
|---------------------------|-----------------------------------|-----------------------------|----------------------|
| `random.random()`         | Random float between 0 and 1     | `random.random()`           | `0.54321` (example)  |
| `random.randint(a, b)`    | Random integer between a and b   | `random.randint(1, 10)`     | `7` (example)        |
| `random.choice(seq)`      | Random element from a sequence   | `random.choice([1, 2, 3])`  | `2` (example)        |
| `random.shuffle(seq)`     | Shuffle a list in-place          | `random.shuffle(my_list)`   | `my_list` shuffled   |
| `random.uniform(a, b)`    | Random float between a and b     | `random.uniform(1, 10)`     | `3.456` (example)    |

---

## Expression Notations
### Infix Notation
- **Definition**: Operators are written between operands (common in math and most programming languages).
- **Example**:
  ```
  A + B
  ```

### Prefix Notation (Polish Notation)
- **Definition**: Operators are written before their operands.
- **Example**:
  ```
  + A B
  ```
- **Usage**: Common in functional programming and calculators.

### Postfix Notation (Reverse Polish Notation)
- **Definition**: Operators are written after their operands.
- **Example**:
  ```
  A B +
  ```
- **Usage**: Used in stack-based computations and certain calculators.

---

## Tips
1. Use `type()` to check the data type of your numbers (e.g., `int`, `float`).
2. Always handle division by zero exceptions using `try` and `except`.
3. Use `Decimal` module for high-precision arithmetic when needed:
   ```python
   from decimal import Decimal
   Decimal('0.1') + Decimal('0.2')
   ```
