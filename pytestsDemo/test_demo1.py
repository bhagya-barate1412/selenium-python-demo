#any pytest file should start with test_
#pytest method names should start with test
#Any code should  be wrapped in method only
#method name should have sense
# -k stands for method names execution, -s for logs in out put -v for more info metadata
#you can run specific file with py.test <filename>
#you can mark(tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#fixtures are used as setup and tear down methids fir test cases- conftest file to generakuze
#fixture and make it available to all test cases

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_fistProgram():
    print("Hello")

def test_SecondGreetCreditCard():
    print("good morning")
