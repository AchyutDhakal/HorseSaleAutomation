def assert_true(condition, message, test, page):
    try:
        assert condition, message   
    except AssertionError as e:
        page.take_screenshot(f"{test}_Assertion_Error")
        raise e

def assert_false(condition, message, test, page):
    try:
        assert not condition, message
    except AssertionError as e:
        page.takescreenshot(f"{test}_Assertion_Error")
        raise e

def assert_equal(actual, expected, message, test , page):
    try:
        assert actual == expected, message
    except AssertionError as e:
        page.takescreenshot(f"{test}_Assertion_Error")
        raise e
    
def assert_not_equal(actual, expected, message, test, page):
    try:
        assert actual != expected, message
    except AssertionError as e:
        page.takescreenshot(f"{test}_Assertion_Error")
        raise e