from USER_INTERFFACE import expected_value
from USER_INTERFFACE import query_string
import pyodbc as pyodbc
from DataTestSuite.Drivers.set_up import fixed_driver

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('../Features/02_Pilot_Food_Pricing.feature', 'Scenario to Validate the Data Test')
def test_pilot_food_pricing(fixed_driver):
    """The User Validates Food Pricing"""
    pass


@given('The User Executes Query', target_fixture="02_validate_data_test")
def execute_query(fixed_driver):
    """The User Executes The Query"""
    global cursor
    conx_string = pyodbc.connect("DRIVER={SQL Server};server=SCIFINSYS;database=sleepstudy;Trusted_Connection=yes;")
    cursor = conx_string.cursor()


@given('The User Receives The Result Set', target_fixture="02_validate_data_test")
def receive_result_set(fixed_driver):
    """The User Receives The Query Results"""
    global query_element

    cursor.execute(query_string)
    query_result = cursor.fetchone()
    for query_element in query_result:
        print(query_element)
@then("Confirm the Results Matches Expected Output", target_fixture="02_validate_data_test")
def validate_result_set(fixed_driver):
    """The User Validates The Results Are As Expected"""
    print(query_element)
    print(expected_value)
    assert expected_value == query_element, "Both are Matching"