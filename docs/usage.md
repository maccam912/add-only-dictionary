# Usage

```python
from add_only_dictionary import AODict

regular_dict: Dict = {"a": 1}
ao_dict: AODict = AODict(regular_dict)

ao_dict["b"] = 2 # works!
ao_dict["a"] = 3 # Nothing happens...
ao_dict["a"] == 1 # True, since the key already existed.
```
