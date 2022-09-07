# Any pytest file should start with test_ or end with _test

# to follow pytest framework standards, whatever code you write, you have to write it in function
# pytest method names should start with test
# every method is treated as 1 test case

# method should be named carefully, so you can use regular expression (-k regex) to select the test cases
# you want to run.

# -s is used for logs in output
# -v is used from more info

# you can run specific file with py.test <filename>

# if you want to run a group of test cases (E.g. those marked for smoke test), you can mark (or tag or group) a set
# of test cases using the @pytest.mark.name_you_give

# to skip a test case, use a registered mark named skip. @pytest.mark.skip

# use @pytest.mark.xfail to execute a test case but not fail it.
# An xfail means that you expect a test to fail for some reason. A common example is a test for a feature not
# yet implemented, or a bug not yet fixed. When a test passes despite being expected to fail
# (marked with pytest.mark.xfail), it’s an xpass and will be reported in the test summary.
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_FirstProgram():
    msg = "hello"
    assert msg == "Hi", "Test Failed because Strs do not match"


def test_SecondProgram(setup):
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"

