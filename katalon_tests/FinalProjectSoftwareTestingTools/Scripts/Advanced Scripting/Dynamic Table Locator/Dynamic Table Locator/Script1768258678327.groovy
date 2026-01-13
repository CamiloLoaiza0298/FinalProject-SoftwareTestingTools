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
import org.openqa.selenium.By as By
import org.openqa.selenium.WebElement as WebElement
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.testobject.ConditionType as ConditionType


WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:8000/products.html')

WebUI.waitForPageLoad(10)

// Create TestObject for products container
TestObject productsContainer = new TestObject()
productsContainer.addProperty('xpath', ConditionType.EQUALS, "//div[@id='products']")

// Wait for the products container to be present
WebUI.waitForElementPresent(productsContainer, 10)

// Create TestObject for product elements
TestObject productElements = new TestObject()
productElements.addProperty('xpath', ConditionType.EQUALS, "//div[@class='img-products']")

// Wait for products to load
WebUI.waitForElementPresent(productElements, 15)

// Create TestObject for T-Rex image using custom XPath
TestObject trexImage = new TestObject()
trexImage.addProperty('xpath', ConditionType.EQUALS, "//div[@id='products']//img[contains(@src,'dino')]")

// Find the WebElement
WebElement productImage = WebUI.findWebElement(trexImage, 10)

// Verify the image is visible
WebUI.verifyElementVisible(trexImage)

WebUI.closeBrowser()