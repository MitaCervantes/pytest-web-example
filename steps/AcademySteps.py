from pages import AcademyPage as page
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion

class AcademySteps(BaseStep):

    def enterUserName(self, username):
     page.getUsernameInput().setText(username)

    def enterPassword(self, password):
     page.getPasswordInput().setText(password)


    def clickLoginButton(self):
     page.getLoginButton().click()

    def validateErrorMessage(self, errorMessage):
     Assertion.assertEquals('Error message was not the expected', errorMessage, page.getErrorMessage().getText())