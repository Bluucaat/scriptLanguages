import pytest
from verem import Verem


def test_verem_muveletek():
    v = Verem()

    # ures teszteles
    assert str(v) == "[]"
    assert v.ures() == True
    assert v.meret() == 0

    # berakasi muvelet
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    assert str(v) == "[1 4 5]"
    assert v.ures() == False
    assert v.meret() == 3

    # pop muvelet
    assert v.kivesz() == 5
    assert str(v) == "[1 4]"
    assert v.kivesz() == 4
    assert v.kivesz() == 1
    assert v.kivesz() == None  # Stack is empty


if __name__ == "__main__":
    pytest.main()
