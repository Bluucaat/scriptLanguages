import pytest
from nyomtatando import print_pages


def test_print_pages():
    assert print_pages("1-4,7,9,11-15") == [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15]
    assert print_pages("5,8,10") == [5, 8, 10]
    assert print_pages("20-25") == [20, 21, 22, 23, 24, 25]
    assert print_pages("2,4-7,10,12-14") == [2, 4, 5, 6, 7, 10, 12, 13, 14]
    assert print_pages("") == []


if __name__ == "__main__":
    pytest.main()
