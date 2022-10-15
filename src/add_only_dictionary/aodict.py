_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class AODict(UserDict[_KT, _VT]):
    def __setitem__(self, k: _KT, v: _VT) -> None:
        super().__setitem__(k, v)