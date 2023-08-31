*** Settings ***
Library    RequestsLibrary
Library  JSONLibrary
Library  Collections
Resource  Resources/UserKeyword.robot

*** Variables ***
${Base_URL}    http://www.testingworldapi.com

*** Test Cases ***
TC_001_Get_Request
    Fetch_and_Validate_Get_Status_code  50  200
    ${response}=     Fetch_and_return_Get_response  50
    log to console  ${response.content}

