# utils/constants.py

# --- System-URL (Anforderung 6) ---
BASE_URL = "https://grocerymate.masterschool.com/"

# --- Testdaten für erfolgreichen Login (Valid) ---
VALID_USER = "riyadhelwalwal@gmail.com"
VALID_PASSWORD = "jEvFyedJe8Fy"

# --- Testdaten für fehlerhaften Login (Invalid) ---
INVALID_USER = "wrong_user@example.com"
INVALID_PASSWORD = "wrong_password"

# --- Testdaten für Altersverifikation ---
TEST_AGE_1987 = "01.05.1987"


# --- Sensitive Testdaten für Bewertungssystem ---
FAKE_CARD = "1234567890123456"
FAKE_CVV = "1234567890"


# --- Testdaten für Bewertungssystem (Über 500 Zeichen Bug) ---
BUG_REVIEW_TEXT = "Das ist ein fehlerhaftes Feedback. " * 20

# --- Testdaten für das Checkout-Formular (Anforderung 9) ---
FIRST_NAME = "Max"
LAST_NAME = "Mustermann"
SHIPPING_ADDRESS = "Hauptstraße 1, 10827 Berlin"

CITY = "Berlin"
POST_CODE = "10827"
EXPIRATION_DATE = "12/2029"
