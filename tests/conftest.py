import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    # Setup: Öffnet den Browser vor jedem Testfall
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver  # Übergibt den Webdriver an den Testfall

    # Teardown: Schließt den Browser ordnungsgemäß nach dem Test
    driver.quit()
