import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_saucedemo_login_aufgabe_1():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. NAVIGIEREN: Öffnet die Login-Seite von SauceDemo
    driver.get("https://saucedemo.com")

    # 3. INTERAKTION: Benutzername und Passwort eingeben
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 4. INTERAKTION: Auf den Login-Button klicken
    driver.find_element(By.ID, "login-button").click()

    # 5. VERIFIKATION: Überprüfen, ob wir auf der Produktseite sind via URL
    assert "inventory.html" in driver.current_url

    # 6. VERIFIKATION: Sicherstellen, dass das Produkt 'Sauce Labs Backpack' sichtbar ist
    backpack = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    assert backpack.is_displayed() == True

    # 7. TEARDOWN: Schließt den Browser am Ende des Tests sauber
    driver.quit()
