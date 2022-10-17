"""Tests for AODict."""
import json

from add_only_dictionary import AODict


def test_instantiate() -> None:
    """Just a sanity check to see if AODict works."""
    ao: AODict = AODict()
    ao["a"] = 1
    assert ao["a"] == 1


def test_no_overwrite() -> None:
    """Make sure if the key is already in the dict, it can't be updated."""
    ao: AODict = AODict()
    ao["a"] = 1
    ao["a"] = 2
    assert ao["a"] == 1


def test_convert_dict_to_aodict() -> None:
    """If a dict is passed in to constructor, convert it to AODict."""
    ao: AODict = AODict({"a": 1})
    assert ao["a"] == 1
    ao["a"] = 2
    assert ao["a"] == 1


def test_nested_dict() -> None:
    """If a value for some key is a dict, convert it to an AODict."""
    ao: AODict = AODict()
    ao["a"] = {"b": 2}
    assert ao["a"]["b"] == 2
    ao["a"]["b"] = 3
    assert ao["a"]["b"] == 2
    ao["a"]["c"] = 3
    assert ao["a"]["c"] == 3


def test_remove_attempt() -> None:
    """Trying to delete a key from a dict should fail."""
    ao: AODict = AODict()
    ao["a"] = 1
    del ao["a"]
    assert ao["a"] == 1


def test_list_methods() -> None:
    """Trying to delete a key from a dict should fail."""
    ao: AODict = AODict({"a": [1, 2, 3]})
    del ao["a"]
    assert ao["a"] == [1, 2, 3]
    ao["a"].pop()
    assert ao["a"] == [1, 2, 3]


def test_json_dumps() -> None:
    """When using json.dumps on an AODict it should behave like regular dict."""
    ao: AODict = AODict()
    ao["a"] = 1
    s = json.dumps(ao)
    assert s == '{"a": 1}'
