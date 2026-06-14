import pytest

@pytest.mark.run(order=1)
def test():
    try:
        from UpgradedInput import UpgradedInput
    except ModuleNotFoundError:
        import pytest; pytest.exit("The UpgradedInput module is missing, please install it before you continue testing!", returncode=1)
