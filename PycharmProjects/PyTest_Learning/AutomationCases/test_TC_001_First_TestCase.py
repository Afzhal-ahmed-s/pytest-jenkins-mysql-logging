import pytest


# test case code must be written in a method
# method name must start with test

a = 100
actualResult = "Afzhal"

# # Decorator
# @pytest.mark.skipif(a>100, reason = "Skipping this functionality for experiment.")
# def test_tc_001_login_logout_testing():
#     print("This is test case code.")
#     print("End of test case.")

@pytest.mark.TopPriority
def test_tc_001_login_logout_testing():
    print("This is Smoke test case code.")
    print("End of test case.")
    assert actualResult == "Afzhal", "These two values must not be same"

@pytest.mark.TopPriority
def test_tc_003_login_logout_invalid_credentials():
    print("This is Sanity tc_003 test case.")
    print("This is the end of test case")