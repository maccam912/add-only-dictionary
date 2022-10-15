"""class AODict."""
from collections import UserDict
from typing import TypeVar


_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class AODict(UserDict[_KT, _VT]):
    """AODict class."""

    def __setitem__(self, k: _KT, v: _VT) -> None:
        """__setitem__."""
        super().__setitem__(k, v)
