import os

import pytest


@pytest.mark.login
def test_regression():
    print("Test_regression")


@pytest.mark.login
def test_sanity():
    print("Test_sanity")


@pytest.mark.login
def test_release():
    print("Test_release")


@pytest.mark.settings
def test_api():
    print("Test_api")


@pytest.mark.login
@pytest.mark.settings
def test_api1():
    print("Test_api1")


@pytest.mark.skip(reason="just testing skip")
def test_release1():
    print("Test_release1")


@pytest.mark.skipif(os.name == 'posix', reason="do not run on mac os")
def test_sanity1():
    print("test_sanity1")

# To run this above tests, open command prompt or terminal & navigate to project directory, type
# pytest .\locators\test_py_test_options.py
# This above command will run all the test methods, but will not print the output to console.
# To print the output, we have to use -s along with pytest
# pytest .\locators\test_py_test_options.py -s
# To print the console output along with specific test names, we can use the pytest option -v [verbose]
# pytest .\locators\test_py_test_options.py -s -v
# Run tests based on string match :
# Run all test class or test methods whose name matches to the string provided with -k parameter
# pytest .\locators\test_py_test_options.py -s -v -k "release"
# Run based on the category match – pytest mark
# To run specific mark or category, we can use the -m parameter
# pytest .\locators\test_py_test_options.py -s -v -m "login"
# Warning: PytestUnknownMarkWarning: Unknown pytest.mark.login - is this a typo?
# To resolve above error, create a pytest.ini file under root directory and
# add all the category or marks under this file
# Note – after “:” it’s optional, you can just add any description
# markers =
#   login:
#   settings:
# Run tests using multiple mark or categories
# To run either login or settings related tests
# pytest .\locators\test_py_test_options.py -s -v -m "login or settings"
# All the above tests will be running.
# To run tests that has both login & settings
# pytest .\locators\test_py_test_options.py -s -v -m "login and settings"
# This above command will only run method – test_api1()
# Exclude or skip tests based on mark
# We can use not prefix to the mark to skip specific tests
# pytest .\locators\test_py_test_options.py -s -v -m "not login"
# This above code will not run tests with mark login
# We can use combination of marks with not, means we can include or exclude specific marks at once
# pytest .\locators\test_py_test_options.py -s -v -m "not login and settings"
# This above command will only run test method test_api()
# Note – you can create different combinations of marks in each test method and run using or
# and operators to get more understanding.
# Skip tests with out pytest options
# using @pytest.mark.skip
# pytest .\locators\test_py_test_options.py -s -v
# This above command will skip the test method – test_release1()
# Skip the test based on a condition
# Pytest provides an option as skipif to use a condition to skip a test,
# if the condition evaluates to true, then only test will skip else run.
# Let’s say, if the os == macos, then skip the test
# pytest .\locators\test_py_test_options.py -s -v
# This above command will run the test method test_regression() if you are running on mac os.
# Note – if mac os, then os.name will give the output as “posix”
# you can evaluate any condition inside the skipif
