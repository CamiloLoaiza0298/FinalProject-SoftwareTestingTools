import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable

TestData registrationData = findTestData('Data Files/registration_invalid')

for (def index : (1..registrationData.getRowNumbers())) {
    WebUI.openBrowser('')
    
    WebUI.navigateToUrl('http://localhost:8000/register.html')
    
    WebUI.setText(findTestObject('Object Repository/Page_Register/username_input'), registrationData.getValue('username', index))
    
    WebUI.setText(findTestObject('Object Repository/Page_Register/email_input'), registrationData.getValue('email', index))
    
    WebUI.setText(findTestObject('Object Repository/Page_Register/age_input'), registrationData.getValue('age', index))
    
    WebUI.setText(findTestObject('Object Repository/Page_Register/password_input'), registrationData.getValue('password', index))
    
    WebUI.setText(findTestObject('Object Repository/Page_Register/confirm_password_input'), registrationData.getValue('confirm_password', index))
    
    WebUI.click(findTestObject('Object Repository/Page_Register/register_button'))
    
   // Verify that the page redirects to created.html
    WebUI.verifyMatch(WebUI.getUrl(), '.*created\\.html.*', true, FailureHandling.CONTINUE_ON_FAILURE)
    
    WebUI.closeBrowser()
}