"""Tests for AOList."""
from add_only_dictionary import AOList


def check_invariants(ao: AOList) -> None:
    """Common checks that shoujld continue being true."""
    assert ao[0] == 1
    assert ao[-1] == 3
    assert len(ao) == 3


def test_methods() -> None:
    """Test the four methods that would normally remove elements."""
    ao: AOList = AOList([1, 2, 3])
    check_invariants(ao)

    del ao[0]
    check_invariants(ao)

    ao.remove(2)
    check_invariants(ao)

    ao.pop()
    check_invariants(ao)

    ao.clear()
    check_invariants(ao)
