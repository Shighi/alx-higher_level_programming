# Python Test-Driven Development

This repository contains Python functions for various tasks designed to practice test-driven development. Each function is implemented with error handling and follows specific requirements.

## Tasks

1. **Integers addition**: A function that adds two integers with type checks and casting.
   - **File**: `0-add_integer.py`
   - **Tests**: `tests/0-add_integer.txt`

2. **Divide a matrix**: A function that divides all elements of a matrix by a given divisor with validation checks.
   - **File**: `2-matrix_divided.py`
   - **Tests**: `tests/2-matrix_divided.txt`

3. **Say my name**: A function that prints a formatted name with error handling for input types.
   - **File**: `3-say_my_name.py`
   - **Tests**: `tests/3-say_my_name.txt`

4. **Print square**: A function that prints a square of a specified size using the `#` character.
   - **File**: `4-print_square.py`
   - **Tests**: `tests/4-print_square.txt`

5. **Text indentation**: A function that formats text by adding new lines after specified punctuation marks.
   - **File**: `5-text_indentation.py`
   - **Tests**: `tests/5-text_indentation.txt`

6. **Max integer**: A function that finds the maximum integer in a list with unittests provided.
   - **File**: `6-max_integer.py`
   - **Tests**: `tests/6-max_integer_test.py`

7. **Matrix multiplication**: A function that multiplies two matrices with validation.
   - **File**: `100-matrix_mul.py`
   - **Tests**: `tests/100-matrix_mul.txt`

8. **Lazy matrix multiplication**: A function that multiplies two matrices using NumPy.
   - **File**: `101-lazy_matrix_mul.py`
   - **Tests**: `tests/101-lazy_matrix_mul.txt`

9. **Python strings**: A C function to print Python string objects with type checks.
   - **File**: `102-python.c`
   - **Tests**: `102-tests.py`

## Usage

To run the tests, use the following command for each task:
```bash
python3 -m doctest tests/<test_file>.txt
