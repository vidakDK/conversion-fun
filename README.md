# Roman Conversion

Library for converting numbers from Roman numerals to Arabic integers.

## Documentation

The conversion algorithms have been optimized for speed.


### Introduction

There are two main functions that reside in the `roman_conversion` module:
function | explanation
-------- | -----------
`int2roman` | Converts integer in the range [1,4999] to a Roman numeral
`roman2int` | Converts a Roman numeral to an integer representation (also [1,4999])

### Usage

In a Python module or console:

```python
from roman_conversion import int2roman, roman2int
foo = 'VIX'
bar = roman2int(foo)
print(bar)
baz = int2roman(bar)
print(baz)
```



### Tests

#### Unit Tests
To run basic unit tests for the main functions:
```bash
python tests/unit_tests.py
```

The tests cover basic usage, edge cases, and sanity checks.

#### Efficiency Tests
In development phase many different algorithms were considered, and timing tests were made to compare their speed.

To run the timing tests:
```bash
python timing_tests.py
```














