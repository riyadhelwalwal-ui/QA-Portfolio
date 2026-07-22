import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_saucedemo_login_and_verify():
    """
    Aufgabe 1: Web-Automatisierung mit Selenium auf SauceDemo.
    Überprüft den erfolgreichen Login und das Vorhandensein des Produkts.
    """
    # 1. SETUP: Startet den Google Chrome Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 2. NAVIGIEREN: Rufe die Ziel-Website auf
        driver.get("https://saucedemo.com")

        # 3. INTERAKTION: Benutzername und Passwort eingeben und einloggen
        # Findet das Eingabefeld für den Benutzernamen und tippt 'standard_user' ein
        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        # Findet das Eingabefeld für das Passwort und tippt 'secret_sauce' ein
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # Klicke auf den Login-Button
        driver.find_element(By.ID, "login-button").click()

        # 4. VERIFIKATION: Überprüfen, ob das Produkt 'Sauce Labs Backpack' sichtbar ist
        # Wir suchen das Element anhand seines exakten Textes auf der Produktseite
        produkt_element = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")

        # Die Assertion: Prüfen, ob das Element tatsächlich auf der Seite angezeigt wird
        assert produkt_element.is_displayed() == True

    finally:
        # 5. TEARDOWN: Schließt den Browser sauber, um Speicherplatz freizugeben
        driver.quit()
