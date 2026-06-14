from typing import Callable, Any
from enum import Enum

class InputTypes(Enum):
    """Types of input, used whenever you want to automatically convert
    the user input into a determined type (Es: Integer)"""
    STRING = 0
    INTEGER = 1
    FLOAT = 2
    BOOL = 3

class UpgradedInput:
    """Main class for the 'Upgraded Input' module.
    
    By default, all callbacks are initialized to None.

    If an EOFError, KeyboardInterrupt, or RuntimeError is encountered 
    in this state the program will exit with status code 1.
    """

    def __init__(self) -> None:
        self.before_input_function: Callable | None = None
        """
        This variable takes any function or None

        If the function is valid it gets called before python's default input gets called

        So it works like this:

        ```python
        your_function()
        return input()
        ```
        """

        self.end_of_file_input_function: Callable | None = None
        """
        This variable takes any function or None

        If the function is valid it gets called when the input function returns either EOFError or KeyboardInterrupt

        So it works like this:

        ```python
        try:
            return input()
        except EOFError, KeyboardInterrupt
            your_function()
        ```
        """


        self.after_input_function: Callable | None = None
        """
        This variable takes any function or None

        If the function is valid it gets called when the input ends getting called

        So it works like this:

        ```python
        text = input()
        your_function()
        conversion() # in case gets parsed
        return text
        ```
        """

        self.runtime_error_function: Callable | None = None
        """
        This variable takes any function or None

        If the function is valid it gets called when input gets called in case sys.stdin gets lost
        
        (as in you do sys.stdin = None for example)

        So it works like this:

        ```python
        try:
            return input()
        except RuntimeError:
            runtime_error_function()
        ```
        """

        self.invalid_user_input_function: Callable | None = None
        """
        This variable takes any function or None

        If the function is valid it gets called when the automatic conversion fails,
        else, at it's default state, exists the program

        So it gets called like this:

        ```python
        text = input()
        try:
            return automatic_conversion(text)
        except ValueError:
            return your_function(text)
        ```
        """

    def input(self, prompt: object = "", type:InputTypes = InputTypes.STRING) -> Any:
        """Original documentation for input:
        
        Read a string from standard input.  The trailing newline is stripped.

        The prompt string, if given, is printed to standard output without a
        trailing newline before reading input.

        If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
        On *nix systems, readline is used if available.

        type: Specifies the automatic conversion
        (Default is InputTypes.STRING so it returns the string)
        """

        before_input_func:Callable | None = self.before_input_function
        exception_func:Callable | None = self.end_of_file_input_function
        after_input_func:Callable | None = self.after_input_function
        runtime_error_func:Callable | None = self.runtime_error_function
        invalid_input_func:Callable | None = self.invalid_user_input_function
        invalid:bool = False
        text:str = ""

        def default_exit():
            print("Exiting...")
            exit(1)
        
        try:
            if callable(before_input_func):
                before_input_func()

            text = input(prompt)
            
            if callable(after_input_func):
                after_input_func()
                
        except (EOFError, KeyboardInterrupt):
            if callable(exception_func):
                exception_func()
                invalid = True
            else:
                default_exit()

        except RuntimeError: # lost sys.stdin
            if callable(runtime_error_func):
                runtime_error_func()
                invalid = True
            else:
                default_exit()
        
        if invalid:
            default_exit()
        
        try:
            match type:
                case InputTypes.STRING:
                    return text
                    
                case InputTypes.INTEGER:
                    return int(text)

                case InputTypes.FLOAT:
                    return float(text)
                
                case InputTypes.BOOL:
                    text_temp = text.lower()
                    if (
                        text_temp == "y" or
                        text_temp == "true" or
                        text_temp == "1"
                    ):
                        return True
                    # in any other case
                    return False
                
        except ValueError:
            if callable(invalid_input_func):
                return invalid_input_func(text)
            else:
                print("Invalid value inserted!")
                default_exit()
