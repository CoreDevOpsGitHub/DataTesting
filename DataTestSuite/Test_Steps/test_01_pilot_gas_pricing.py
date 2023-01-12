import USER_INTERFFACE
from USER_INTERFFACE import *

import pyodbc as pyodbc
from DataTestSuite.Drivers.set_up import fixed_driver

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('../Features/01_Pilot_Gas_Pricing.feature', 'Scenario to Validate the Data Test')
def test_pilot_gasstation_pricing():
    """The User Validates Pilot Pricing"""



@given('The User Intake Form Is Opened', target_fixture="01_validate_data_test")
def open_input_form():
    """Open Input Form"""

    # Open Form To Extract Values
    global app
    app = USER_INTERFFACE.App()
    app.mainloop()


@when('The Form Information is Extracted', target_fixture='01_validate_data_test')
def form_information_extracted():
    global query_string
    global expected_value

    # Extract Query String
    query_string = app.query_string_value

    # Extract Expected Value
    expected_value = app.expected_value


@when('The User Executes Query', target_fixture="01_validate_data_test")
def execute_query():
    # Create Connection String
    conx_string = pyodbc.connect(
        "DRIVER={SQL Server};server=EC2AMAZ-O7K498H\SQLEXPRESS;database=sleepstudy;Trusted_Connection=yes;")

    # Create Cursor
    cursor = conx_string.cursor()

    # Execute Query
    cursor.execute(query_string)

    # Extract Results
    global query_element
    query_result = cursor.fetchone()
    for query_element in query_result:
        print(query_element)


@then("Confirm the Results Matches Expected Output", target_fixture="01_validate_data_test")
def validate_result_set():
    """The User Validates The Results Are As Expected"""


    assert int(expected_value) == query_element, "Both are Matching"

