# Python - Almost a Circle

This project implements a series of Python classes that model geometric shapes, focusing on rectangles and squares. It's part of the Higher Level Programming curriculum at ALX.

## Features

- Base class for managing id attribute
- Rectangle class inheriting from Base
- Square class inheriting from Rectangle
- Implements attribute validation, area calculation, and display methods
- JSON and CSV serialization/deserialization
- Unittest suite for all classes and methods

## Requirements

- Python 3.8.5
- pycodestyle 2.8.*
- Unittest module

## Usage

Import the classes and use them in your Python scripts:

```python
from models.rectangle import Rectangle
from models.square import Square

r1 = Rectangle(10, 7, 2, 8)
s1 = Square(5)

print(r1)
print(s1)
```

Run the test suite:

```
python3 -m unittest discover tests
```

## File Structure

- `models/`: Contains the main classes (Base, Rectangle, Square)
- `tests/`: Contains all unit tests
