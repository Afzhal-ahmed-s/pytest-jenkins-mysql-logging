*** Settings ***
Library         RequestsLibrary
Library         JSONLibrary
Library         Collections


*** Variables ***
${Base_URL}      http://www.testingworldapi.com/

*** Test Cases ***
TC_005_create_new_resource
    Create Session         Add_Data       ${Base_URL}
    &{body}=              Create Dictionary   first_name=Afzhal     middle_name=Ahmed   last_name=S     date_of_birth=12/12/2002
    &{header}=            create dictionary  Content-Type=application/json
    ${response}=           POST On Session    Add_Data     /api/studentDetails     data=${body}     headers=${header}
    ${actual_status_code}=  Convert To String    ${response.status_code}
#    ${json_response}=      ${response.content.json()}
#    @{name_list}=          Get Value From Json  ${json_response}    data[0].first_name
#    ${name}=               Get From List    ${name_list}    0
#    Should Be Equal        ${actual_status_code}  200
#    Should Be Equal        ${name}    Eve
    Log To Console         ${response.status_code}
    Log To Console         ${response.content}
