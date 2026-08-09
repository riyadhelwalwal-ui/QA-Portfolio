import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# =====================================================================
# FIXTURE: Startet den Browser einmal für alle Tests (Effizienz)
# =====================================================================
@pytest.fixture(scope="session")
def browser():
    """
    Diese Fixture startet den Chrome-Browser einmal für die gesamte Test-Session
    und schließt ihn am Ende sauber (Teardown).
    """
    # Setup: Startet den echten Google Chrome Browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Übergibt den Browser temporär an die Testfunktionen (Linie bleibt offen)
    yield driver
    
    # Teardown: Schließt den Browser am Ende der Session
    driver.quit()


# =====================================================================
# AUFGABE 1 & 2: Login-Test mit Parametrisierung für alle Benutzer
# =====================================================================
@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user"
])
def test_saucedemo_login_flow(browser, username):
    """
    Testet den Login-Prozess für alle verfügbaren Benutzertypen auf SauceDemo.
    Verifiziert entweder den erfolgreichen Login oder die korrekte Fehlermeldung.
    """
    # 1. Navigiere zur Ziel-Website
    browser.get("https://www.saucedemo.com/")
    
    # 2. Felder vor jedem Login-Versuch leeren (Clean State)
    user_field = browser.find_element(By.ID, "user-name")
    pass_field = browser.find_element(By.ID, "password")
    user_field.clear()
    pass_field.clear()
    
    # 3. Interaktion: Zugangsdaten aus der Tabelle eingeben
    user_field.send_keys(username)
    pass_field.send_keys("secret_sauce")
    
    # 4. Klicke auf den Login-Button
    browser.find_element(By.ID, "login-button").click()
    
    # 5. Verifikation (Assert): Je nach Benutzertyp prüfen
    if username == "locked_out_user":
        # Wenn der Benutzer gesperrt ist, muss eine Fehlermeldung sichtbar sein
        error_message = browser.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_message.is_displayed() == True
    else:
        # Für alle anderen Benutzer: Prüfen, ob das Produkt 'Sauce Labs Backpack' vorhanden ist
        backpack_product = browser.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
        assert backpack_product.is_displayed() == True
        
        # Überprüfen, ob wir uns auf der korrekten Produktseite befinden via URL
        assert "inventory.html" in browser.current_url
