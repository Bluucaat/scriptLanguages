import pytest
from zarojelek import helyeszarojel  # Replace "your_module" with the actual name of your module

def test_helyeszarojel():
    #helyesek
    assert helyeszarojel("((5+3)*2+1)") == True
    assert helyeszarojel("{[(3+1)+2]+}") == True
    assert helyeszarojel("(3+{1-1})") == True


    # helytelenek
    assert helyeszarojel("(5+3)*2+1)") == False
    assert helyeszarojel("((5+3)*2+1))") == False
    assert helyeszarojel("(({[(((1)-2)+3)-3]/3}-3)") == False

if __name__ == "__main__":
    pytest.main()