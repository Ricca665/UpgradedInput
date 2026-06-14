def test():
    from UpgradedInput import UpgradedInput, InputTypes
    import builtins

    inp = UpgradedInput()

    # all tester functions
    def string_tester(x):
        assert isinstance(x, str), "Input is returning the wrong type"
        assert x == "yes", "Input is returning the wrong value"

    def integer_tester(x):
        assert isinstance(x, int), "The automatic conversion for integer is returning the wrong type"
        assert x == 1, "The automatic conversion for integer is returning the wrong value"
    
    def float_tester(x):
        assert isinstance(x, float), "The automatic conversion for floats is returning the wrong type"
        assert x == 1.0, "The automatic conversion for integer is returning the wrong value"
    
    def bool_tester_true(x):
        assert isinstance(x, bool), "The automatic conversion for bools is returning the wrong type"
        assert x == True, "The automatic conversion didn't return the valid value"
    
    def bool_tester_false(x):
        assert isinstance(x, bool), "The automatic conversion for bools is returning the wrong type"
        assert x == False, "The automatic conversion didn't return the valid value"
        
    types = [
        {"type": InputTypes.STRING, "value": "yes", "call": string_tester},
        {"type": InputTypes.INTEGER, "value": "1", "call": integer_tester},
        {"type": InputTypes.FLOAT, "value": "1.0", "call": float_tester},
        {"type": InputTypes.BOOL, "value": "y", "call": bool_tester_true},
        {"type": InputTypes.BOOL, "value": "n", "call": bool_tester_false},
    ]

    # main function to execute when testing user input
    def get_input(i, type):
        og_input = builtins.input
        builtins.input = lambda x: i
        get_input = inp.input(type=type)
        builtins.input = og_input
        return get_input

    # loop and call every function
    for type in types:
        type["call"](get_input(type["value"], type["type"]))
