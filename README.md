# Roman Conversion

Library for converting numbers from Roman numerals to Arabic integers and vice versa.


## Introduction

There are two main functions that reside in the `roman_conversion` module:

function | description
-------- | -----------
`int2roman` | Converts integer in the range [1,4999] to a Roman numeral
`roman2int` | Converts a Roman numeral to an integer representation (also [1,4999])

## Usage

In a Python module or console:

```python
from roman_conversion import int2roman, roman2int
foo = 'XIV'
bar = roman2int(foo)
print(bar)  # prints 14
baz = int2roman(bar)
print(baz)  # prints XIV
```

## Tests

### Unit Tests
To run basic unit tests for the main functions:
```bash
python tests/unit_tests.py
```

The tests cover basic usage, edge cases, and sanity checks.

### Efficiency Tests
In development phase many different algorithms were considered, and timing tests were made to compare their speed.

To run the timing tests:
```bash
python timing_tests.py
```

## Acknowledgements

Thanks to the `roman` package creator Mark Pilgrim (mark@diveintopython.org) 
for unit test ideas and validity check regex.













