import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# =====================================================================
# FIXTURE: Startet den Browser NEU vor jedem einzelnen Test (Isolierung)
# =====================================================================
@pytest.fixture(scope="function")
def browser():
    """
    Diese Fixture startet den Chrome-Browser vor jedem Testfall neu,
    um eine saubere und isolierte Testumgebung zu garantieren.
    """
    # Setup: Startet den Google Chrome Browser und macht das Fenster groß
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Übergibt den Browser temporär an die Testfunktion
    yield driver

    # Teardown: Schließt den Browser nach dem Test sauber
    driver.quit()


# =====================================================================
# PARAMETRISIERUNG: Tabelle mit (Username, Password) für ALLE 6 Benutzertypen
# =====================================================================
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])
# =====================================================================
# TESTFALL: Dynamischer Login-Test mit datengetriebener Verifikation
# =====================================================================
def test_saucedemo_login_flow(browser, username, password):
    """
    Testet den Login-Prozess für alle verfügbaren Benutzertypen auf SauceDemo.
    Verifiziert entweder den erfolgreichen Login via URL oder die exakte Fehlermeldung.
    """
    # 1. Navigiere zur Ziel-Website
    browser.get("https://saucedemo.com")

    # 2. Interaktion: Zugangsdaten kommen BEIDE dynamisch aus der Tabelle oben
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    # 3. Verifikation (Assert): Präzise Prüfung je nach Benutzertyp
    if username == "locked_out_user":
        # Hier suchen wir direkt nach dem h3-Tag, wo der Text wirklich drinnen steht
        error_element = browser.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_element.is_displayed() == True
        assert "locked out" in error_element.text.lower()
    else:
        # Für alle anderen 5 funktionierenden User: URL-Prüfung auf die Produktseite
        assert "inventory.html" in browser.current_url
