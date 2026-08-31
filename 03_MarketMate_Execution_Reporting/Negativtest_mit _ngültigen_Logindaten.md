📑 Testbericht: Authentifizierung - Testfall 4 (Negativtest mit ungültigen Logindaten)

### 🔗 Testfall-ID: MM-AU-02 (Fehlermeldung bei falschem Benutzernamen/Passwort)

#### 🔗 1. Genaue Schritte zur Reproduktion/Ausführung:
1. Öffnen Sie die GroceryMate-Webseite.
2. Klicken Sie auf das Profil-Symbol (Account-Icon) oben rechts, um die Login-Maske zu öffnen.
3. Geben Sie im Feld "Username" eine ungültige E-Mail-Adresse ein (z.B. riyad_wrong@test.com).
4. Geben Sie im Feld "Password" ein falsches Passwort ein (z.B. WrongPassword123!).
5. Klicken Sie auf die Schaltfläche "Login".

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Das System muss den Zugriff verweigern, den Benutzer auf der Login-Seite halten und eine gut sichtbare rote Fehlermeldung (z.B. "Invalid credentials" oder "Error") auf der Benutzeroberfläche anzeigen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[UI-VALIDIERUNG ERFOLGREICH]:** Das System blockiert den unberechtigten Zugriff erfolgreich. Der Benutzer wird nicht eingeloggt und eine entsprechende Fehlermeldung erscheint auf dem Bildschirm.

#### 🔗 4. Status: PASSED 🟢 (Soll- und Ist-Verhalten stimmen exakt überein)
<img width="909" height="431" alt="Screenshot 2026-08-31 211410" src="https://github.com/user-attachments/assets/d3d957fd-5c18-4fd0-8428-023f768d3a9a" />
