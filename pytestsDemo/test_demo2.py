import pytest


@pytest.mark.smoke
def test_fistProgram():
    msg = "hello"
    assert msg == "Hi","Test failed because strings do not match"


@pytest.mark.xfail
def test_SecondCreditCard():
    a=4
    b=6
    assert a+2==6, "addition do not match"

