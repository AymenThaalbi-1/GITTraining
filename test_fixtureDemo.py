# What are fixtures in Pytest
# Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to
# feed some data to the tests such as database connections, URLs to test and some sort of input data.

# defining fixture
import pytest


# @pytest.fixture()
# def setup():
#    print("I will be executing first as defined as fixture")
## if you want to run post execution test, you do not need to create a new fixture, however, use yield which will
## mean to pytest : execute this after executing the test
#    yield
#    print("i will be executed after test execution")

## you have to pass the fixture method name as an argument to your test to make it aware about the dependency
# def test_fixture_demo(setup):
#    print("i will execute steps in fixture demo method")

# commented for next lecture
######################################
# below you can use the fixture in conftest and optimize your code by calling it only once (use it if you are sure
# you will need for all your test cases.
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo1(self):
        print("i will execute steps in fixture demo method1")
        print("Developper 2 has added this line to the code")

    def test_fixture_demo2(self):
        print("i will execute steps in fixture demo method2")

    def test_fixture_demo3(self):
        print("i will execute steps in fixture demo method3")
