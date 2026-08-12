# 📑 Testbericht: Altersverifikation - Testfall 3 (Grenzwertanalyse exakt 18 Jahre)

### 🔗 Testfall-ID: MM-AV-03 (Grenzwertprüfung für Benutzer von exakt 18 Jahren - Geburtsjahr 2008)

#### 🔗 1. Genaue Schritte (Ausführungsschritte):
1. Öffnen Sie die MarketMate-Homepage und klicken Sie auf die Schaltfläche „Shop“.
2. Das Pop-up-Fenster zur Altersverifikation erscheint auf der Benutzeroberfläche.
3. Geben Sie das Geburtsdatum „13.08.2008“ ein (Benutzer ist heute exakt 18 Jahre alt) und klicken Sie auf „Bestätigen“.
4. Überprüfen Sie, ob das System den Zugriff auf den Webshop und die Kategorie „Alkoholische Getränke“ freigibt.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten):
Da der Benutzer exakt 18 Jahre alt ist, muss das System den Zugriff erfolgreich erlauben. Das Pop-up-Fenster sollte sich schließen und alle Kategorien müssen ohne Fehlermeldung freigegeben werden.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[BUG GEFUNDEN]:** Das System berechnet das Alter fälschlicherweise als minderjährig und zeigt auch bei exakt 18-jährigen Benutzern die UI-Fehlermeldung `"You are underage"` an. Der Zugriff auf Alkohol bleibt gesperrt, obwohl der Benutzer das gesetzliche Mindestalter erreicht hat.

#### 🔗 4. Status: FAIL 🔴 (Fehler in der Grenzwert-Logik für exakt 18 Jahre dokumentiert)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)

**1. Eingabe der Testdaten (Vorher):*

<img width="1818" height="871" alt="Screenshot 2026-08-13 011728" src="https://github.com/user-attachments/assets/194f6afb-2bbd-4a83-b599-a83fc54cb956" />


**2. System-Reaktion und Fehlermeldung (Nachher):**

<img width="4000" height="3000" alt="1000052678" src="https://github.com/user-attachments/assets/405a35e2-3c90-4a49-99f5-a8f0e1b4bbd1" />
