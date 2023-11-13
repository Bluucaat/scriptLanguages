import pytest
from ekezet import ekezetTorles

def test_ekezetTorles():
    input_text = "álmá"
    expected_output = "alma"
    assert ekezetTorles(input_text) == expected_output

    input_text = "banán és alma"
    expected_output = "banan es alma"
    assert ekezetTorles(input_text) == expected_output

    input_text = "a csodállatos python test programom kiveszi az ékezetet"
    expected_output = "a csodallatos python test programom kiveszi az ekezetet"
    assert ekezetTorles(input_text) == expected_output


if __name__ == "__main__":
    pytest.main()