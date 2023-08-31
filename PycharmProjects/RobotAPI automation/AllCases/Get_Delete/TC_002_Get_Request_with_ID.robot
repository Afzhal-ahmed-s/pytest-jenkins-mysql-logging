*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library  Collections
Default Tags  Hi

*** Variables ***
${Base_URL}    http://www.testingworldapi.com/
${Student_ID}    2

*** Test Cases ***
TC_001_Fetch_Student_details_by_ID
    [Tags]  Smoke Sanity
    create session  FetchData  ${Base_URL}
    ${response}=    GET On Session  FetchData     api/sudentDetails/${Student_ID}
    ${actual_response_code}=    convert to string   ${response.status_code}
    log to console  ${Base_URL}
    log to console  ${response.content}
    should be equal  ${actual_response_code}    200

    ${json_response}=   ${response.content.json()}

    @{first_name_list}=    get value from json    ${json_response}  data.first_name
    ${first_name}=  get from list  ${first_name_list}   0
    log to console  ${first_name}
    should be equal  ${first_name}  Test1

    @{last_name_list}=    get value from json    ${json_response}  data.last_name
    ${last_name}=  get from list  ${last_name_list}   0
    log to console  ${last_name}
    should be equal  ${last_name}  Automation

TC_002_Fetch_Student_details_by_ID_2
#    [Tags]  Smoke
    create session  FetchData  ${Base_URL}
    ${response}=    GET On Session  FetchData     api/sudentDetails/${Student_ID}
    ${actual_response_code}=    convert to string   ${response.status_code}
    log to console  ${Base_URL}
    log to console  ${response.content}
    should be equal  ${actual_response_code}    200
