# VRas Helper

This package contains useful functions for working with Python, including basic console text formatting and other useful utilities.

## Contents

- `work_here()`: A function to change the working directory to the location of the current Python script.
- `colorbank`: A class containing ANSI escape codes for text color formatting.
- `ctext`: A class containing escape codes for various console text formatting options.

## Installation

```bash
pip install git+https://github.com/Revo1999/vrashelper
```


## Usage

To use this package, you can simply import the functions and classes you need into your Python scripts:

```python
import vrashelper

# Example usage
work_here()
print(vh.colorbank.hackergreen + "Hello, world!" + vh.colorbank.default)
print(vh.ctext.bold + "This text is bold." + vh.ctext.default)
```

## To uninstall

```bash
pip uninstall vrashelper
```