import pytest
#  Test Case code must be written inside a method
#  Method name must be started with test

@pytest.fixture(scope="module")
def fixture_code():
    print("This is our Fixture Code will execute before testcase")
    print("-----------------------------------------------------")
    yield
    print("Close DB Connection after executing testcase")
    print("-----------------------------------------------------")

@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_Login_Logout_Testing(fixture_code):
    print("This is Smoke Test Case.....")
    print("This is end of my test cases")

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_Login_Logout_Invalid_Credentials(fixture_code):
    print("This is Sanity Test Case")
    print("This is End of testcase")


#  Print statement output display on console   -s
#  Verbose mode -  display test cases name with status    -v