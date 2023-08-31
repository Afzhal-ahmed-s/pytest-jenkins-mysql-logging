import pytest
#  Test Case code must be written inside a method
#  Method name must be started with test

actual_result="Hello"

#Decorator
#@pytest.mark.skipif(a>100,reason="Skipping as this functionality is not working, developer will fix it in new build")

@pytest.mark.TopPriority
def test_tc_001_Login_Logout_Testing():
    print("This is Smoke Test Case.....")
    print("This is end of my test cases")
    assert actual_result != "Hello", "These 2 values must not be same"

@pytest.mark.TopPriority
def test_tc_003_Login_Logout_Invalid_Credentials():
    print("This is Sanity Test Case")
    print("This is End of testcase")


#  Print statement output display on console   -s
#  Verbose mode -  display test cases name with status    -v