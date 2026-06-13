# UpgradedInput
A better, minimal input() wrapper for python


Features compared to python's default input()
- Supports hooks for functions (Before and after input, on exception and on runtime error)

# How to use
Install the module
```
pip install UpgradedInput
```

Use the module
Example:
```python
from UpgradedInput.main import UpgradedInput

# initialize
inp = UpgradedInput()

# Example of hooks (All of them can be left at the dafult state (None))
def before():
    print("Before!")

def after():
    print("After!")

def exception():
    print("Exception!")

def runtime_error():
    print("Runtime error!")

# Initialize the hooks
inp.before_input_function = before
inp.after_input_function = after
inp.exception_close_input_function = exception
inp.runtime_error_function = runtime_error

print(inp.input()) # final call to the wrapper
```
