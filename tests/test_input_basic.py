def test():
    from UpgradedInput import UpgradedInput
    import builtins

    inp = UpgradedInput()

    og_input = builtins.input

    def get_input(i):
        builtins.input = lambda x: i
        get_input = inp.input()
        builtins.input = og_input
        return get_input

    assert get_input("yes") == "yes", "Input is returning the wrong value"

