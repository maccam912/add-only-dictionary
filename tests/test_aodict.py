"""Tests for AODict."""
from add_only_dictionary import AODict


def test_instantiate() -> None:
    """Just a sanity check to see if AODict can be created."""
    ao: AODict[str, int] = AODict()
    ao["a"] = 1
