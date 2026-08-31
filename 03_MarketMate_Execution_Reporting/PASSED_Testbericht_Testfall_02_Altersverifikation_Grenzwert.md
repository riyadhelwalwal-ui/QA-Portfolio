📑 Testbericht: Altersverifikation - Testfall 3 (Grenzwertanalyse exakt 18 Jahre)

### 🔗 Testfall-ID: MM-AV-03 (Grenzwertprüfung für Benutzer von exakt 18 Jahren - Geburtsjahr 2008)

#### 🔗 1. Genaue Schritte (Ausführungsschritte):
1. Öffnen Sie die MarketMate-Homepage.
2. Klicken Sie auf die Schaltfläche „Shop“, um das Alters-Pop-up zu öffnen.
3. Geben Sie das Geburtsdatum ein (Benutzer ist exakt 18 Jahre alt) und klicken Sie auf „Confirm“.
4. Überprüfen Sie, ob das System den Zugriff auf die Kategorie „Alkoholische Getränke“ freigibt.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten):
Da der Benutzer exakt 18 Jahre alt ist, muss das System den Zugriff erfolgreich erlauben. Das Pop-up-Fenster sollte sich schließen und alle Kategorien müssen ohne Fehlermeldung freigegeben werden.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[BUG GEFUNDEN]:** Das System berechnet das Alter fälschlicherweise als minderjährig und zeigt auch bei exakt 18-jährigen Benutzern die UI-Fehlermeldung "You are underage" an. Der Zugriff auf Alkohol bleibt gesperrt, obwohl der Benutzer das gesetzliche Mindestalter erreicht hat.

#### 🔗 4. Status: FAIL 🔴 (Fehler in der Grenzwert-Logik für exakt 18 Jahre dokumentiert)

#### 🔗 5. 🤖 Automatisierter Nachweis (PyTest-Erweiterung):
Das Testskript `test_age_verification.py` schlug bei der Grenzwertprüfung exakt fehl und hat den Bug per Automation bestätigt:
-> AssertionError: assert "You are underage" not in browser.page_source


<img width="1818" height="871" alt="Screenshot 2026-08-13 011728" src="https://github.com/user-attachments/assets/194f6afb-2bbd-4a83-b599-a83fc54cb956" />


**2. System-Reaktion und Fehlermeldung (Nachher):**

<img width="4000" height="3000" alt="1000052678" src="https://github.com/user-attachments/assets/405a35e2-3c90-4a49-99f5-a8f0e1b4bbd1" />
