"""Tests for AODict."""
from add_only_dictionary import AODict


def test_instantiate() -> None:
    """Just a sanity check to see if AODict works."""
    ao: AODict[str, int] = AODict()
    ao["a"] = 1
    assert ao["a"] == 1


def test_no_overwrite() -> None:
    """Make sure if the key is already in the dict, it can't be updated."""
    ao: AODict[str, int] = AODict()
    ao["a"] = 1
    ao["a"] = 2
    assert ao["a"] == 1
