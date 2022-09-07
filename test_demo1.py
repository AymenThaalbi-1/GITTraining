# Any pytest file should start with test_ or end with _test

# to follow pytest framework standards, whatever code you write, you have to write it in function
# pytest method names should start with test
# every method is treated as 1 test case

def test_FirstTestCase(setup):
    print("Hello")
    pint("Developper 2 has changed this")


def test_SecondTestCase():
    print("tester")


def test_crossbrowser(crossbrowser):
    print(crossbrowser)
