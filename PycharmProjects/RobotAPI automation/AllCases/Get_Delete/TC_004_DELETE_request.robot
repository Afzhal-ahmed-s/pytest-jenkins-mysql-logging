*** Settings ***
Library         RequestsLibrary
Library         JSONLibrary
Library         Collections
Library         RequestsLibrary
Library         JSONLibrary
Library         Collections

*** Variables ***
${Base_URL}      https://reqres.in

*** Test Cases ***
TC_004 Validate Delete Request
    Create Session         AppAccess       ${Base_URL}
    ${response}=    delete on session    AppAccess     /api/studentsDetails/1
    ${actual_status_code}=  Convert To String    ${response.status_code}
#    ${json_response}=      ${response.content.json()}
#    @{name_list}=          Get Value From Json  ${json_response}    data[0].first_name
#    ${name}=               Get From List    ${name_list}    0
    Should Be Equal        ${actual_status_code}  204
#    Should Be Equal        ${name}    Eve
    Log To Console         ${response.status_code}
    Log To Console         ${response.content}
