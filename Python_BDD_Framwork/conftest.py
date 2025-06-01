import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def setupDriver(request):
    browser = getattr(request, "param", "Chrome")
    if browser == "Chrome":
        chrome_options = Options()
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