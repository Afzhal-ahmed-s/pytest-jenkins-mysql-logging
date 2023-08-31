*** Settings ***
Library         RequestsLibrary
Library         JSONLibrary
Library         Collections

*** Variables ***
${Base_URL}      https://reqres.in

*** Test Cases ***
TC_003 Validate Get Request with Parameters
    [Tags]  Smoke    Regression
    Create Session         Get_Param       ${Base_URL}
    &{param}=              Create Dictionary   page=2
    ${response}=           GET On Session     Get_Param     /api/users   params=${param}
    ${actual_status_code}=  Convert To String    ${response.status_code}
    ${json_response}=      ${response.content.json()}
    @{name_list}=          Get Value From Json  ${json_response}    data[0].first_name
    ${name}=               Get From List    ${name_list}    0
    Should Be Equal        ${actual_status_code}  200
    Should Be Equal        ${name}    Eve
    Log To Console         ${response.status_code}
    Log To Console         ${response.content}
