import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:8000/shop.html')

WebUI.click(findTestObject('Page_Shop/button_PROCEED TO CHECKOUT'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Full name_full-name'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Email_email'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Address_address'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_City_city'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Postal code_postal'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Cardholder name_card-name'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Card number_card-number'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_Expiry_expiry'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/input_CVV_cvv'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/button_Cancel'))

WebUI.verifyElementVisible(findTestObject('Page_Checkout/button_Place order'))

WebUI.closeBrowser()

