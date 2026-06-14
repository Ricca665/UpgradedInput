import pytest

@pytest.mark.run(order=2)
def test():
    from UpgradedInput import UpgradedInput
    
    inp = UpgradedInput()

    assert isinstance(inp, UpgradedInput), "UpgradedInput initialized wrongly, please fix"
