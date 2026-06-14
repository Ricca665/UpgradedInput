# UpgradedInput
A better, minimal input() wrapper for python

Features compared to python's default input()
- Supports hooks for functions (Before and after input, on exception and on runtime error)
- Supports automatic conversion with validation

# How to use
Install the module
```
pip install UpgradedInput
```

Use the module
Example:
```python
from UpgradedInput import UpgradedInput, InputTypes
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

def invalid_user_input(text):
    print(text)
    return None

# Initialize the hooks
inp.before_input_function = before
inp.after_input_function = after
inp.end_of_file_input_function = exception
inp.runtime_error_function = runtime_error # say we lost sys.stdin or something else that triggers a runtime error
inp.invalid_user_input_function = invalid_user_input

print(inp.input()) # final call to the wrapper
print(inp.input(prompt="insert text: ")) # supports prompt (from input)

# in case the automatic conversion fails, in this example it calls invalid_user_input 
# which prints what the user typed, and returns None in this example (REFER TO DOCUMENTATION!!!!!!!!)
print(inp.input(type=InputTypes.INTEGER)) # supports automatic conversion!
print(inp.input(type=InputTypes.FLOAT)) # floats
print(inp.input(type=InputTypes.BOOL)) # booleans
```
