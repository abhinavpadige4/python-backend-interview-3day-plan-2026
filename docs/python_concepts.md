# Python Concepts for Backend Interviews

## Object-Oriented Programming (OOP)

### Classes and Objects
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
```

### Inheritance
- **Single Inheritance**: Child class inherits from one parent
- **Multiple Inheritance**: Child class inherits from multiple parents
- **Multilevel Inheritance**: Child inherits from parent, which inherits from grandparent
- **Hierarchical Inheritance**: Multiple children inherit from same parent
- **Hybrid Inheritance**: Combination of multiple types

### Polymorphism
```python
def animal_sound(animal):
    print(animal.make_sound())

# Works with any object that has make_sound method
animal_sound(Dog("Buddy", "Golden Retriever"))
```

### Encapsulation
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return 0
    
    def get_balance(self):
        return self.__balance
```

### Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

## Design Patterns

### Singleton Pattern
```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def connect(self):
        # Connection logic
        pass
```

### Factory Pattern
```python
class NotificationSender:
    def send(self, message):
        pass

class EmailSender(NotificationSender):
    def send(self, message):
        # Send email logic
        pass

class SMSSender(NotificationSender):
    def send(self, message):
        # Send SMS logic
        pass

class NotificationFactory:
    @staticmethod
    def create_sender(notification_type):
        if notification_type == "email":
            return EmailSender()
        elif notification_type == "sms":
            return SMSSender()
        else:
            raise ValueError("Unknown notification type")
```

### Observer Pattern
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer notified: {subject}")
```

### Decorator Pattern
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y
```

## Generators and Iterators

### Generators
```python
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Usage
for num in fibonacci_generator(10):
    print(num)
```

### Generator Expressions
```python
squares = (x*x for x in range(10))
sum_of_squares = sum(squares)
```

## Decorators

### Function Decorators
```python
def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done"
```

### Class Decorators
```python
def add_method(cls):
    def new_method(self):
        return "Added method"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass
```

## Context Managers

### Using `with` Statement
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

### Context Manager Decorator
```python
from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwargs):
    resource = acquire_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        release_resource(resource)
```

## Error Handling

### Exception Hierarchy
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    └── TypeError
```

### Custom Exceptions
```python
class ValidationError(Exception):
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    pass
```

### Try-Except-Else-Finally
```python
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Value error: {e}")
    return default_value
except PermissionError:
    logger.error("Permission denied")
    raise
else:
    logger.info("Operation succeeded")
finally:
    cleanup_resources()
```

## Testing

### Unit Testing with unittest
```python
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        self.assertEqual(s.split(','), ['hello world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

### Testing with pytest
```python
def test_addition():
    assert add(2, 3) == 5

def test_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("x,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
])
def test_square(x, expected):
    assert square(x) == expected
```

## Concurrency

### Threading
```python
import threading
import time

def worker(name, delay):
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} finished")

# Create threads
t1 = threading.Thread(target=worker, args=('A', 2))
t2 = threading.Thread(target=worker, args=('B', 1))

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()
```

### Thread Safety
```python
import threading

class Counter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def get_value(self):
        with self._lock:
            return self._value
```

### Asyncio
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_url(session, 'http://example.com'),
            fetch_url(session, 'http://httpbin.org/get')
        ]
        results = await asyncio.gather(*tasks)
        return results

# Run the async function
# asyncio.run(main())
```

## File I/O

### Reading Files
```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

### Writing Files
```python
# Write string
with open('output.txt', 'w') as f:
    f.write('Hello, World!')

# Write lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)

# Append to file
with open('log.txt', 'a') as f:
    f.write(f'{timestamp}: {message}\n')
```

### Working with CSV
```python
import csv

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Writing CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    writer.writeheader()
    writer.writerow({'name': 'John', 'age': 30, 'city': 'NYC'})
```

### Working with JSON
```python
import json

# Reading JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Writing JSON
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)
```

## Regular Expressions

### Basic Patterns
```python
import re

# Match digits
pattern = r'\d+'
matches = re.findall(pattern, 'abc123def456')

# Match email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(email_pattern, 'test@example.com'):
    print('Valid email')

# Substitution
cleaned = re.sub(r'\s+', ' ', 'Hello   World')
```

### Compiled Patterns
```python
# Compile for reuse
pattern = re.compile(r'\b[A-Z][a-z]+\b')
matches = pattern.findall('Hello World from Python')
```

## Virtual Environments and Packaging

### Creating Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
```

### Managing Dependencies
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
pip list
pip show package_name
```

### Creating Packages
```
mypackage/
├── __init__.py
├── core.py
├── utils.py
└── tests/
    ├── __init__.py
    └── test_core.py
```

### Setup.py
```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="Your Name",
    description="A sample Python package",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
```