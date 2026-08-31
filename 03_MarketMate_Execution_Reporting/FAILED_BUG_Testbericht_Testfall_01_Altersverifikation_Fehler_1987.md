📑 Testbericht: Altersverifikation - Testfall 1 (Fehlerhafte Altersberechnung)

### 🔗 Testfall-ID: MM-AV-01 (Fehlerhafte Altersberechnung für Geburtsjahr 1987)

#### 🔗 1. Genaue Schritte (Ausführungsschritte):
1. Öffnen Sie die MarketMate-Homepage.
2. Klicken Sie oben im Header auf das Benutzer-Profil-Symbol (Account Icon).
3. Loggen Sie sich mit den gültigen Testdaten ein und navigieren Sie zum Shop.
4. Geben Sie im Pop-up-Fenster zur Altersverifikation das Geburtsdatum „01.05.1987“ ein und klicken Sie auf „Confirm“.
5. Versuchen Sie, die Kategorie „Alkoholische Getränke“ zu öffnen.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten):
Das System muss das Alter korrekt als über 18 Jahre berechnen. Das Pop-up-Fenster sollte sich schließen und der Zugriff auf alle Kategorien (einschließlich Alkohol) muss ohne Fehlermeldung freigegeben werden.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[BUG GEFUNDEN]:** Das System berechnet das Alter fälschlicherweise als minderjährig, zeigt die UI-Fehlermeldung "You are underage" an und sperrt den Zugriff auf die Alkohol-Kategorie für einen volljährigen Nutzer (1987).

#### 🔗 4. Status: FAIL 🔴 (Fehler in der Altersberechnungs-Logik dokumentiert)

#### 🔗 5. 🤖 Automatisierter Nachweis (PyTest-Erweiterung):
Das Testskript `test_age_verification.py` schlug bei der Verifikation fehl und hat den Bug erfolgreich per Automation bestätigt:
-> AssertionError: assert "You are underage" not in browser.page_source
