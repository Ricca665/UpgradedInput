from typing import Callable

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

    def input(self, prompt: object = "") -> str:
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

        def default_exit():
            print("Exiting...")
            exit(1)

        try:
            if callable(before_input_func):
                before_input_func()

            text = input(prompt)

            if callable(after_input_func):
                after_input_func()

            return text
        
        except (EOFError, KeyboardInterrupt):
            if callable(exception_func):
                exception_func()
            else:
                default_exit()

        except RuntimeError: # lost sys.stdin
            if callable(runtime_error_func):
                runtime_error_func()
            else:
                default_exit()
        
        return ""
