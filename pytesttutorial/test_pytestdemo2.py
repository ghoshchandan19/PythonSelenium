import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def testmethod1(setUp):
    print("this is test method 1")

def testmethod2(setUp):
    print("this is test method 2")
