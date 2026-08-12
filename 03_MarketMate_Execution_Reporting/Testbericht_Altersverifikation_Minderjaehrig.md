# 📑 Testbericht: Altersverifikation - Testfall 2 (Minderjähriger Benutzer)

### 🔗 Testfall-ID: MM-AV-02 (Zugriffsprüfung für minderjährige Benutzer - Geburtsjahr 2012)

#### 🔗 1. Genaue Schritte (Ausführungsschritte):
1. Öffnen Sie die MarketMate-Homepage und klicken Sie auf die Schaltfläche „Shop“.
2. Das Pop-up-Fenster zur Altersverifikation erscheint auf der Benutzeroberfläche.
3. Geben Sie das Geburtsdatum „01.01.2012“ ein und klicken Sie auf „Bestätigen“.
4. Versuchen Sie, die Kategorie „Alkoholische Getränke“ zu öffnen.
5. Navigieren Sie zu normalen Produkten (z. B. Schokolade / Snacks) und prüfen Sie die Browsing-Möglichkeit.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten):
Das System muss das Alter als minderjährig (14 Jahre) erkennen und die Fehlermeldung `"You are underage"` anzeigen. Der Zugriff auf die Kategorie „Alkoholische Getränke“ muss strikt blockiert bleiben. Das Kaufen von normalen Produkten (wie Schokolade) soll jedoch erlaubt sein.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
Das System zeigt die Fehlermeldung `"You are underage"` korrekt an. Der Zugriff auf die Kategorie „Alkoholische Getränke“ wird erfolgreich blockiert. Wie erwartet, kann der Benutzer weiterhin im Webshop surfen und normale Produkte (Schokolade/Snacks) ansehen und kaufen.

#### 🔗 4. Status: PASS 🟢 (Erwartetes Verhalten für minderjährige Benutzer erfolgreich verifiziert)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)
<!-- Ziehen <img width="4000" height="3000" alt="1000052677" src="https://github.com/user-attachments/assets/d81bd94c-5f63-46a4-bb9a-3851bb3f82d6" />
Sie Ihren Screenshot für den 14-jährigen Testfall per Drag & Drop hierher -->
