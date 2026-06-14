def test():
    from UpgradedInput import UpgradedInput
    import builtins
    # hackiest of hack to test hooks

    # the way this works in the following
    # 1. Initialize the UpgradedInput module
    # 2. Save the original input function
    # 3. Replace the input function with a lambda function (that can return anything really)
    # 4. Initialize all of our hooks
    # 5. Call the final input function
    # 6. Reset the builtins.input to the original function
    # By replacing the input function it's like we automatically typed in something
    # Now, every time our hook function gets called it increases a global counter by 1
    # Which then simply allows us to check how many times our hook function got called

    # Step 1, 2 and 3
    inp = UpgradedInput()
    og_input = builtins.input
    builtins.input = lambda x: "stuff"

    # hacky way to set/get a global counter in local scope
    globals()["counter"] = 0
    
    def hook(x="a"):
       globals()["counter"] += 1 
    
    # Step 4
    inp.before_input_function = hook
    inp.after_input_function = hook
    inp.end_of_file_input_function = hook
    inp.invalid_user_input_function = hook
    inp.runtime_error_function = hook
    
    # Step 5
    inp.input()

    # we reset the og input just in case
    builtins.input = og_input

    # then we can check how many times it got called
    count = globals()["counter"]
    if count < 2:
        assert 1==2, "One or more hooks didn't get called"

