"""class AODict."""
from typing import TypeVar


K = TypeVar("K")
V = TypeVar("V")


class AODict(dict[K, V]):
    """AODict class."""

    def __setitem__(self, k: K, v: V) -> None:
        """__setitem__."""
        super().__setitem__(k, v)
