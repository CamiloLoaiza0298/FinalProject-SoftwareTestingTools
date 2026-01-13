import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import internal.GlobalVariable as GlobalVariable
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.testobject.ConditionType as ConditionType
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:8000/index.html')

WebUI.waitForPageLoad(10)

// Get viewport dimensions from execution profile with defaults
int width = 1920
int height = 1080
try {
    width = Integer.parseInt(GlobalVariable.VIEWPORT_WIDTH)
} catch (MissingPropertyException e) {
    WebUI.comment("VIEWPORT_WIDTH not found, using default: 1920")
}
try {
    height = Integer.parseInt(GlobalVariable.VIEWPORT_HEIGHT)
} catch (MissingPropertyException e) {
    WebUI.comment("VIEWPORT_HEIGHT not found, using default: 1080")
}

// Set the browser viewport size
WebUI.setViewPortSize(width, height)

WebUI.comment("Testing viewport: ${width}x${height}")

// Create TestObjects for responsive elements
TestObject navWeb = new TestObject()
navWeb.addProperty('xpath', ConditionType.EQUALS, "//div[@class='nav-web']")

TestObject navMobile = new TestObject()
navMobile.addProperty('xpath', ConditionType.EQUALS, "//div[@class='nav-mobile']")

TestObject hamburgerMenu = new TestObject()
hamburgerMenu.addProperty('xpath', ConditionType.EQUALS, "//a[@class='icon']")

// Check responsive behavior based on viewport size
if (width >= 768) {
    // Desktop: expect web navigation visible, mobile navigation hidden
    WebUI.verifyElementVisible(navWeb, FailureHandling.CONTINUE_ON_FAILURE)
    WebUI.verifyElementNotVisible(navMobile, FailureHandling.CONTINUE_ON_FAILURE)
    WebUI.comment("Desktop layout verified: Web navigation visible, mobile navigation hidden")
} else {
    // Tablet/Mobile: expect mobile navigation visible
    WebUI.verifyElementVisible(navMobile, FailureHandling.CONTINUE_ON_FAILURE)
    WebUI.verifyElementVisible(hamburgerMenu, FailureHandling.CONTINUE_ON_FAILURE)
    WebUI.comment("Mobile layout verified: Mobile navigation and hamburger menu visible")
}

// Additional responsiveness checks
TestObject heroImage = new TestObject()
heroImage.addProperty('xpath', ConditionType.EQUALS, "//img[@src='media/header.png']")

WebUI.verifyElementVisible(heroImage, FailureHandling.CONTINUE_ON_FAILURE)

// Check if content fits viewport (no horizontal scroll)
WebUI.verifyElementNotPresent(new TestObject().addProperty('xpath', ConditionType.EQUALS, "//body[contains(@style,'overflow-x')]"), 5, FailureHandling.CONTINUE_ON_FAILURE)

WebUI.comment("Viewport test completed for ${width}x${height}")

WebUI.closeBrowser()