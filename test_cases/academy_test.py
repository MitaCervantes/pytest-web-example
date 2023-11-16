from pytest_bdd import when, then, scenarios
from steps.AcademySteps import AcademySteps as steps

scenarios('../features/AcademyLogin.feature')

@when('enter username <username>')
def enterUserName(username):
    steps().enterUserName(username)

@when('enter password <password>')
def enterPassword(password):
    steps().enterPassword(password)

@when('click login button')
def clickLogin():
    steps().clickLoginButton()

@then('validate error message <errorMessage>')
def validateErrorMessage(errorMessage):
    steps().validateErrorMessage(errorMessage)

def teardown_function():
    steps().closeBrowser()