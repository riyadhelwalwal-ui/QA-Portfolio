# 📑 Hausaufgabe 2 - XPath Lösungen & Web-Elemente Dokumentation

## 🔗 Testumgebung (Target URL Reference)
* **Offizielle Testseite:** [https://grocerymate.masterschool.com](https://grocerymate.masterschool.com)
* **QA Engineer:** Riyadh Elwalwal

---

## 🌐 Teil 1: Navigation und Header-Elemente (Hauptseite)

### 1. Schreibe das XPath für das im untenstehenden Bild hervorgehobene Symbol/den hervorgehobenen Button.
* **Beschreibung:** Der hervorgehobene Benutzer-Profil-Button (User/Account Icon) im Header der Seite.
* **XPath:** `//div[contains(@class, 'header')]//a[contains(@href, 'auth')]` oder `//div[@class='headerIcon']`

---

## 🔐 Teil 2: Authentifizierung & Login-Formular (/auth)

### 2. Schreibe das XPath für alle Eingabefelder, die "Sign In"-Schaltfläche, den Link "Create a new account" und den Link "Go to Home".

* **E-Mail-Eingabefeld (Email address):**
  * **XPath:** `//input[@type='email' or @placeholder='Email address']`
* **Passwort-Eingabefeld (Password):**
  * **XPath:** `//input[@type='password' or @placeholder='Password']`
* **"Sign In"-Schaltfläche (Button):**
  * **XPath:** `//button[text()='Sign In']`
* **Link "Create a new account":**
  * **XPath:** `//a[text()='Create a new account']`
* **Link "Go to Home":**
  * **XPath:** `//a[text()='Go to Home']`

---

## 📝 Teil 3: Registrierungs-Formular (Sign Up)

### 3. Klicke nun auf denselben Link wie in Teil 2 auf "Create a new account", dann wirst du die folgende Benutzeroberfläche sehen: Schreibe das XPath für alle Eingabefelder und die "Sign Up"-Schaltfläche.

* **Vollständiger Name Eingabefeld (Full Name):**
  * **XPath:** `//input[@type='text' and @placeholder='Full Name']`
* **E-Mail-Eingabefeld (Email address):**
  * **XPath:** `//input[@type='email' and @placeholder='Email address']`
* **Passwort-Eingabefeld (Password):**
  * **XPath:** `//input[@type='password' and @placeholder='Password']`
* **"Sign Up"-Schaltfläche (Button):**
  * **XPath:** `//button[text()='Sign Up']`

---

## 🔞 Teil 4: Altersverifikation Pop-up (Modal)

### 4. Schreibe das XPath der "Confirm"-Schaltfläche, die du im Modal sehen kannst.
* **Beschreibung:** Der Bestätigungs-Button im Pop-up-Sperrfenster für die Altersprüfung.
* **XPath:** `//div[contains(@class, 'modal')]//button[text()='Confirm']` oder `//button[contains(text(), 'Confirm')]`

---

## 🛒 Teil 5: Shop-Seite und Produkt-Interaktionen (/store)

### 5. Gehe zur Shop-Seite und schreibe das XPath für das Mengeneingabefeld von Orangen, die "Add to cart"-Schaltfläche für Orangen und die "Add to wish list"-Schaltfläche für Orangen.

* **Mengeneingabefeld für Orangen (Quantity Input):**
  * **XPath:** `//div[div/h3[text()='Oranges']]//input[@type='number']`
* **"Add to cart"-Schaltfläche für Orangen (In den Warenkorb):**
  * **XPath:** `//div[div/h3[text()='Oranges']]//button[text()='Add to cart']`
* **"Add to wish list"-Schaltfläche für Orangen (Herz-Symbol / Favoriten):**
  * **XPath:** `//div[div/h3[text()='Oranges']]//button[contains(@class, 'wishlist') or .//svg]`
