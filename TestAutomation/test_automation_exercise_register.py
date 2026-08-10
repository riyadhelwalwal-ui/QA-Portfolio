import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# =====================================================================
# FIXTURE: Browser-Setup und Teardown für den Registrierungstest
# =====================================================================
@pytest.fixture(scope="function")
def driver():
    """
    Diese Fixture startet den Chrome-Browser vor dem Testfall,
    maximiert das Fenster und schließt ihn am Ende sauber (Teardown).
    """
    # 1. Browser starten und maximieren
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    # 18. Browser am Ende sauber schließen
    browser.quit()


# =====================================================================
# TESTFALL: Vollständiger E2E Registrierungs- und Löschungsprozess
# =====================================================================
def test_user_registration_and_deletion(driver):
    """
    Aufgabe 3: Automatisiert den kompletten Lebenszyklus eines Benutzers
    (Registrierung, Daten ausfüllen, Verifikation und Account löschen).
    """
    # 2. Zur URL navigieren
    driver.get("http://automationexercise.com")

    # 3. Überprüfen, dass die Startseite erfolgreich sichtbar ist
    assert "Automation Exercise" in driver.title

    # 4. Auf die營Schaltfläche „Signup / Login“ klicken
    driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()

    # 5. Überprüfen, dass „New User Signup!“ sichtbar ist
    signup_heading = driver.find_element(By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    assert signup_heading.is_displayed() == True

    # 6. Namen und E-Mail-Adresse eingeben (Eindeutige Daten nutzen)
    driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys("Riad Tester")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("riad_qa_berlin2026@test.com")

    # 7. Auf die Schaltfläche „Signup“ klicken
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    # 8. Überprüfen, dass „ENTER ACCOUNT INFORMATION“ sichtbar ist
    info_heading = driver.find_element(By.XPATH, "//b[contains(text(), 'Enter Account Information')]")
    assert info_heading.is_displayed() == True

    # 9. Details ausfüllen: Titel (Mr.), Passwort, Geburtsdatum
    driver.find_element(By.ID, "id_gender1").click()  # Wählt 'Mr.'
    driver.find_element(By.ID, "password").send_keys("SecurePassword123!")

    # Geburtsdatum via Dropdown-Interaktion ausfüllen
    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("April")
    driver.find_element(By.ID, "years").send_keys("1995")

    # 10. Kontrollkästchen „Sign up for our newsletter!“ auswählen
    driver.find_element(By.ID, "newsletter").click()

    # 11. Kontrollkästchen „Receive special offers von Partnern“ auswählen
    driver.find_element(By.ID, "optin").click()

    # 12. Details ausfüllen: Vorname, Nachname, Firma, Adresse, Land, Stadt, Postleitzahl, Handynummer
    driver.find_element(By.ID, "first_name").send_keys("Riad")
    driver.find_element(By.ID, "last_name").send_keys("Elwalwal")
    driver.find_element(By.ID, "company").send_keys("Masterschool QA")
    driver.find_element(By.ID, "address1").send_keys("Hauptstraße 12")
    driver.find_element(By.ID, "country").send_keys("Germany")
    driver.find_element(By.ID, "state").send_keys("Berlin")
    driver.find_element(By.ID, "city").send_keys("Berlin")
    driver.find_element(By.ID, "zipcode").send_keys("10115")
    driver.find_element(By.ID, "mobile_number").send_keys("+491761234567")

    # 13. Auf die Schaltfläche „Create Account“ klicken
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    # 14. Überprüfen, dass „ACCOUNT CREATED!“ sichtbar ist
    created_heading = driver.find_element(By.XPATH, "//b[contains(text(), 'Account Created!')]")
    assert created_heading.is_displayed() == True

    # 15. Auf die Schaltfläche „Continue“ klicken
    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

    # 16. Überprüfen, dass „Logged in as username“ sichtbar ist
    logged_in_text = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")
    assert logged_in_text.is_displayed() == True

    # 17. Auf die Schaltfläche „Delete Account“ klicken (Teardown der Testdaten)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Delete Account')]").click()

    # 18. Überprüfen, dass „ACCOUNT DELETED!“ sichtbar ist und auf „Continue“ klicken
    deleted_heading = driver.find_element(By.XPATH, "//b[contains(text(), 'Account Deleted!')]")
    assert deleted_heading.is_displayed() == True
    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
