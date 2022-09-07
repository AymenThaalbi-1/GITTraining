# The conftest.py file serves as a means of providing fixtures for an entire directory. Fixtures defined
# in a conftest.py can be used by any test in that package without needing to import them (pytest will
# automatically discover them). We can define the fixture functions in this file to make them accessible
# across multiple test files.

# the conftest file must be named as its name and this is how python will now this is the conf file for your test.
import pytest


# Use the below scope= in case you want to run the fixtures only at class level and not for every test case.
# @pytest.fixture(scope="class")
@pytest.fixture()
def setup():
    print("I will be executing first as defined as fixture")
    yield
    print("i will be executed after test execution")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


# to achieve parameterization (Parameterizing of a test is done to run the test against multiple sets of inputs)
@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossbrowser(request):
    return request.param
