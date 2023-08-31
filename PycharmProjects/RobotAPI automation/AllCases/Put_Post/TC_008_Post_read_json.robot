*** Settings ***
Library         RequestsLibrary
Library         JSONLibrary
Library         Collections
Library  ../../ReadContent/ReadJSON_content.py
Resource  ../../Resources/UserKeyword.robot


*** Variables ***
${Base_URL}      http://www.testingworldapi.com/

*** Test Cases ***
TC_005_create_new_resource
    Create Session         Add_Data       ${Base_URL}
    &{header}=            create dictionary  Content-Type=application/json
    ${jsonContent}=    Fetch_request_content
    log to console  ${jsonContent}

    ${response}=           POST On Session    Add_Data     /api/studentDetails     data=${jsonContent}     headers=${header}
    ${actual_status_code}=  Convert To String    ${response.status_code}
    Log To Console         ${response.status_code}
    Log To Console         ${response.content}