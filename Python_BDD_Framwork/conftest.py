import pytest
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