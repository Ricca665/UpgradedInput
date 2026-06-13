from typing import Callable, Any
from enum import Enum

class InputTypes(Enum):
    """Types of input, used whenever you want to verify if the user input is of determined type (Es: integer)"""
    STRING = 0
    INTEGER = 1
    FLOAT = 2
    BOOL = 3

class UpgradedInput:
    """Main class for the 'Upgraded input' module.
    
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

        self.exception_close_input_function: Callable | None = None
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
        
        (as in you so sys.stdin = None)

        So it works like this:

        ```python
        try:
            return input()
        except RuntimeError:
            runtime_error_function()
        ```
        """

    def input(self, prompt: object = "", type:InputTypes = InputTypes.STRING) -> Any:
        """Original documentation for input:
        
        Read a string from standard input.  The trailing newline is stripped.

        The prompt string, if given, is printed to standard output without a
        trailing newline before reading input.

        If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
        On *nix systems, readline is used if available.
        """

        before_input_func:Callable | None = self.before_input_function
        exception_func:Callable | None = self.exception_close_input_function
        after_input_func:Callable | None = self.after_input_function
        runtime_error_func:Callable | None = self.runtime_error_function
        invalid:bool = False
        text = ""

        def default_exit():
            print("Exiting...")
            exit(1)
        
        try:
            if callable(before_input_func):
                before_input_func()

            def call_after_func():
                if callable(after_input_func):
                    after_input_func()

            text = input(prompt)
            call_after_func()
                
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
            print("Invalid value inserted!")
            default_exit()
