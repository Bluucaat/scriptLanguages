import pytest
from hamming import hamming_distance

def test_hamming_distance_same_strings():
    assert hamming_distance("toned", "roses") == 3
    assert hamming_distance("bone", "gone") == 1
    assert hamming_distance("little", "litlle") == 1

def test_hamming_distance_empty_strings():
    assert hamming_distance("", "") == 0

