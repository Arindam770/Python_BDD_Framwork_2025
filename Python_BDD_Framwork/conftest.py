import pytest
import os
import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def setupDriver(request):
    browser = getattr(request, "param", "Chrome")
    if browser == "Chrome":
        chrome_options = Options()
        prefs = {
       "credentials_enable_service": False,
       "profile.password_manager_enabled": False,
       "profile.password_manager_leak_detection": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-web-security")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver

    driver.close()
    driver.quit()

def pytest_generate_tests(metafunc):
    if "setupDriver" in metafunc.fixturenames:
        metafunc.parametrize("setupDriver", ["Chrome", "Firefox"], indirect=True)


# Optional: Create screenshots directory once
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    os.makedirs("Python_BDD_Framwork\\SupportFiles\\screenShot", exist_ok=True)

# Create reports directory
@pytest.fixture(scope="session", autouse=True)
def create_reports_dir():
    os.makedirs("Python_BDD_Framwork\\reports\\allure-report", exist_ok=True)
    os.makedirs("Python_BDD_Framwork\\reports\\allure-results", exist_ok=True)

# 📸 Hook: Take screenshot after every BDD step
@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    outcome = yield
    try:
        driver = request.getfixturevalue("setupDriver")
        
        # Only capture screenshot if driver fixture is used
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            step_name = step.name.replace(" ", "_")
            filename = f"Python_BDD_Framwork/SupportFiles/screenShot/{step_name}_{timestamp}.png"
            
            driver.save_screenshot(filename)
            allure.attach.file(filename, name=step.name, attachment_type=AttachmentType.PNG)
            
            # Add step details to Allure report
            allure.dynamic.description(f"Step: {step.name}")
            allure.dynamic.title(f"Scenario: {scenario.name}")
            allure.dynamic.feature(feature.name)
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

# Add hook for generating Allure report after test session
@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    try:
        import subprocess
        results_dir = "Python_BDD_Framwork/reports/allure-results"
        report_dir = "Python_BDD_Framwork/reports/allure-report"
        
        # Generate Allure report
        subprocess.run(["allure", "generate", results_dir, "-o", report_dir, "--clean"], check=True)
        print(f"\nAllure report generated successfully in: {report_dir}")
    except Exception as e:
        print(f"Failed to generate Allure report: {str(e)}")