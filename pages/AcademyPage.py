from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def getUsernameInput():
    return UIElement(By.ID,'user-name')

def getPasswordInput():
    return UIElement(By.ID,'password')

def getLoginButton():
    return UIElement(By.ID,'login-button')

def getErrorMessage():
    return UIElement(By.XPATH,'//h3[@data-test="error"]')

