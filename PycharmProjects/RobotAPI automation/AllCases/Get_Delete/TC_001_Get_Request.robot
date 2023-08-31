*** Settings ***
Library    RequestsLibrary
Documentation  This suite is for learning purpose only.
Resource  ../../Resources/UserKeyword.robot
Force Tags  Hello

*** Variables ***
${Base_URL}    http://www.testingworldapi.com

*** Test Cases ***
TC_001_Get_Request
    [Setup]  Welcome_User
    [Teardown]  End_TestCase
    [Documentation]  This test case if for demonstarting GET request
    create session  Get_Student_Details  ${Base_URL}
    ${response}=    GET On Session  Get_Student_Details     api/sudentDetails
    log to console  ${Base_URL}
    log to console  ${response.status_code}
    log to console  ${response.content}


