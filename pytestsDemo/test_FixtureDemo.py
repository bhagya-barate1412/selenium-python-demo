import pytest


@pytest.fixture()

def setup():
    print("I will be execute first")
    yield
    print("I will be execute last")

def test_FixtureDemo(setup):
    print("I will be execute steps FixtureDemo method")

