"""
data_pipeline_mini

A simple demonstration of a lazy data pipeline using Python generators.

Pipeline:
    Fibonacci Generator
        ↓
    Square Transformation
        ↓
    Even Number Filter
        ↓
    Take First 5 Results (islice)
        ↓
    Print Output

Concepts demonstrated:
- Infinite generators
- Lazy evaluation
- Generator-based transformations
- Generator-based filtering
- Chaining iterators together
- Using itertools.islice to limit an infinite sequence

The entire pipeline processes values one at a time without creating
intermediate lists, making it memory efficient and demonstrating the
power of Python's iterator protocol.
"""

from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def transform_square(iterable):
    for i in iterable:
        yield i * i

def filter_even(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i

def slice_first_15(iterable):
    yield from islice(iterable, 5)


numbers = fibonacci()
squared_numbers = transform_square(numbers)
even_numbers = filter_even(squared_numbers)
result = slice_first_15(even_numbers)

print(list(result))
