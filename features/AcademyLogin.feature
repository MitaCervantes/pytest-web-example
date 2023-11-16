Feature: Academy Login

    @academy
    Scenario Outline: Login fails
        When enter username <username>
        And enter password <password>
        And click login button
        Then validate error message <errorMessage>

    Examples:
        | username        | password     | errorMessage                                       |
        | standard_user   |              | Epic sadface: Password is required                 |
        | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out. |
        |                 | secret_sauce | Epic sadface: Username is required                 |