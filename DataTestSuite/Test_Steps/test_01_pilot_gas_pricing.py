from USER_INTERFFACE import show_entry_fields

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
def test_pilot_gasstation_pricing(fixed_driver):
    """The User Validates Pilot Pricing"""


@given('The User Executes Query', target_fixture="01_validate_data_test")
def execute_query(fixed_driver):
    """The User Executes The Query"""
    global cursor
    conx_string = pyodbc.connect("DRIVER={SQL Server};server=EC2AMAZ-O7K498H\SQLEXPRESS;database=sleepstudy;Trusted_Connection=yes;")
    cursor = conx_string.cursor()


@given('The User Receives The Result Set', target_fixture="01_validate_data_test")
def receive_result_set(fixed_driver):
    """The User Receives The Query Results"""
   # global query_element
    #exec = show_entry_fields()
    exec = show_entry_fields().expected_value_string
    print(exec)
    #print(show_entry_fields())
   # cursor.execute()
   # query_result = cursor.fetchone()
   # for query_element in query_result:
   #     print(query_element)


@then("Confirm the Results Matches Expected Output", target_fixture="01_validate_data_test")
def validate_result_set(fixed_driver):
    """The User Validates The Results Are As Expected"""
    #print(query_element)
    #print(expected_value_string)
    #assert expected_value_string == query_element, "Both are Matching"