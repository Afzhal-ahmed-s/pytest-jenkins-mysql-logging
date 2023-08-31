*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library  ../ReadContent/ReadJSON_content.py

*** Variables ***
${Base_URL}      http://www.testingworldapi.com/


*** Keywords ***
Fetch_and_Validate_Get_Status_code
    [Arguments]  ${studentId}   ${expected_status_code}
    [Documentation]  This key word is for validating status code of given student
    [Timeout]   .1s
    [Setup]  Welcome_User
    [Teardown]  End_TestCase
    create session  SName   ${Base_URL}
    ${response}=    get on session  SName   /api/studentDetails/${studentId}
    ${statusCode}=  convert to string  ${response.status_code}
    should be equal  ${expected_status_code}    ${statusCode}

Fetch_and_return_Get_response
    [Arguments]  ${studentId}
    create session  SName   ${Base_URL}
    ${response}=    get on session  SName   /api/studentDetails/${studentId}
    [Return]  ${response}

Fetch_request_content
    ${jsonBody}=    read_request_content
    [Return]  ${jsonBody}

Welcome_User
    [Documentation]  Executing new test case
    log to console  This is the start of testCase

End_TestCase
    [Documentation]  TestCase completed
    log to console  This is the start of testCase


