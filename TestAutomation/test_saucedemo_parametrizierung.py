import pytest
from pygments.styles.pastie import PastieStyle
from selenium import webdriver
from selenium.webdriver.common.by import By


# FIXTURE: Startet den Browser einmal für alle Testfälle (Zentrales Setup)
@pytest.fixture(scope="function")
def browser():
    """
    Diese Fixture startet den Chrome-Browser vor jedem Testfall neu,
    um eine saubere und isolierte Testumgebung zu garantieren.
    """
    # Setup: Startet den Google Chrome Browser und macht das Fenster groß
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Übergibt den Browser temporär an die Testfunktion (Linie bleibt offen)
    yield driver

    # Teardown: Schließt den Browser nach dem Test sauber
    driver.quit()

# PARAMETRISIERUNG: Tabelle mit allen vier Benutzertypen von SauceDemo
@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user"
])
def test_saucedemo_login_flow(browser, username):
    # 1. Navigiere zur Ziel-Website
    browser.get("https://saucedemo.com")

    # 2. Interaktion: Zugangsdaten eingeben (Benutzername kommt dynamisch aus der Tabelle)
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys("secret_sauce")

    # 3. Klicke auf den Login-Button
    browser.find_element(By.ID, "login-button").click()

    # 4. Verifikation (Assert): Präzise Prüfung je nach Benutzertyp
    if username == "locked_out_user":
        # Hier suchen wir direkt nach dem h3-Tag, wo der Text wirklich drinnen steht
        error_element = browser.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_element.is_displayed() == True
        assert "locked out" in error_element.text.lower()
    else:
        # Für alle funktionierenden User: URL-Prüfung, ob wir auf der Produktseite sind
        assert "inventory.html" in browser.current_url


