import pytest


# test case code must be written in a method
# method name must start with test

@pytest.fixture(scope = "module")
def fixtureCode():
    print("This is fixture code, will execute before testcase.")
    print("-------------------------------------")
    yield
    print("Close browser after executing testcase.")

# Decorator
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_login_logout_testing(fixtureCode):
    print("This is Smoke case code.")
    print("End of test case.")

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_login_logout_invalid_credentials(fixtureCode):
    print("This is Sanity test case.")
    print("This is the end of test case")

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_login_logout_invalid_credentials_dup(fixtureCode):
    print("This is Sanity test case.")
    print("This is the end of test case")