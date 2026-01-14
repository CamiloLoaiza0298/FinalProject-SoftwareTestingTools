# Final Project - Software Testing Tools
Final Project for Software Testing Tools course, Matrix College of Technology Inc. - Juan Camilo Loaiza Alarcon.

**Project Title**: Final Project - Software Testing Tools

**Description**: This repository contains a small sample website and automated test suites implemented with two tools:
- Katalon Studio, under `katalon_tests/FinalProjectSoftwareTestingTools`
- Python + Selenium tests, under `selenium_tests/`

The project was created by Juan Camilo Loaiza Alarcon as part of the course deliverables. It includes the static website used for testing, Selenium-based pytest suites, helper utilities, and a Katalon Studio test project.

**Website: Local Setup & Run**
- Prerequisites: Python 3 (for the simple static server) and a modern browser (Mozilla Firefox or Google Chrome prefered).
- To run the website locally (serves the `website/` folder on port 8000):

```bash
cd website
python3 -m http.server 8000
```
Then open http://localhost:8000 in your browser.

**Testing Environments**

**Python / Selenium (pytest)**
- Prerequisites: Python 3 and a browser (Chrome / Firefox). Chromedriver or geckodriver is required.
- Recommended Python packages:

```bash
pip install pytest selenium webdriver-manager openpyxl
```

- Running the tests:

```bash
cd selenium_tests
pytest
```
If you want to use a specific browser (Firefox or Chrome) you can use these commands instead:

```bash
cd selenium_tests
pytest --browser chrome
```

```bash
cd selenium_tests
pytest --browser firefox
```

- Notes:
	- The Selenium tests are located in `selenium_tests/tests/` and use utilities in `selenium_tests/utils/` (for example `WebDriverFactory.py`).
	- Ensure your local browser version is compatible with the installed driver.
	- The report generated with the selenium tests is saved in the `results/` folder.

**Katalon Studio**
- Prerequisites: Katalon Studio (recommended recent stable release) and Java JDK if required by your Katalon version.
- Open the Katalon project:

	1. Launch Katalon Studio.
	2. Choose File → Open Project and select the folder `FinalProject-SoftwareTestingTools/katalon_tests/FinalProjectSoftwareTestingTools`.
	3. The project contains Test Cases, Test Suites, Object Repository, and settings; the main suite is `Final Project Test Suite`.

**Important**
- For some tests (Invalid Registration Data Driven) Katalon Studio needs test data, which is included in a Data File (registration_invalid (1)), but to do this, the Data File needs to be binded to an Excel file, which path changes when you dowload it from the repository to your PC. That's why you need to:

	1. Launch Katalon Studio and open the project
	2. Expand "Data Files"
	3. Double click "registration_invalid(1)"
	4. In the new window search for the "File Name" and click "Browse"
	5. Browse the Excel file in the "Data Files" directory (FinalProject-SoftwareTestingTools/katalon_tests/FinalProjectSoftwareTestingTools/Data Files/registration_invalid.xlsx)

- Running Katalon tests:
	- Use the Katalon GUI to run Test Suites.
	- Test reports and execution logs are written to the project's `Reports/` directory inside the Katalon project.

**Project Structure**
- `website/` — static HTML/CSS/JS pages used for test scenarios.
- `selenium_tests/` — pytest suites, pages, utilities, and test data.
- `katalon_tests/FinalProjectSoftwareTestingTools/` — Katalon Studio project files.

---
Assignment: 420-TZ4-GX SOFTWARE TESTING TOOLS
Written by: Juan Camilo Loaiza Alarcon - 6805001