# 📑 Testbericht: Altersverifikation - Testfall 1 (Fehlerhafte Altersberechnung)

### 🔗 Testfall-ID: MM-AV-01 (Fehlerhafte Altersberechnung für Geburtsjahr 1987)

#### 🔗 1. Genaue Schritte (Ausführungsschritte):
1. Öffnen Sie die MarketMate-Homepage und klicken Sie auf die Schaltfläche „Shop“.
2. Das Pop-up-Fenster zur Altersverifikation erscheint auf der Benutzeroberfläche.
3. Geben Sie das Geburtsdatum „01.05.1987“ ein und klicken Sie auf „Bestätigen“.
4. Versuchen Sie, die Kategorie „Alkoholische Getränke“ zu öffnen.
5. Navigieren Sie zu normalen Produkten (z. B. Celery / Ginger) und legen Sie diese in den Warenkorb.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten):
Das System muss das Alter korrekt als über 18 Jahre berechnen. Das Pop-up-Fenster sollte sich schließen, der Zugriff auf alle Kategorien (einschließlich Alkohol) muss freigegeben werden und es darf keine Fehlermeldung erscheinen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[BUG GEFUNDEN]:** Das System berechnet das Alter fälschlicherweise als minderjährig und zeigt die UI-Fehlermeldung `"You are underage"` an. Der Zugriff auf die Alkohol-Kategorie bleibt gesperrt. Das Durchsuchen und Einkaufen von normalen Produkten (Celery/Ginger) wird jedoch trotz der Fehlermeldung fälschlicherweise erlaubt.

#### 🔗 4. Status: FAIL 🔴 (Fehler in der Altersberechnungs-Logik dokumentiert)

---

## **2. Anhang: Nachweis (Visual Evidence)**

**1. Eingabe der Testdaten (Vorher):**

<img width="4000" height="3000" alt="1000052677" src="https://github.com/user-attachments/assets/468e4c69-8f89-40b5-8307-959aafcaa00e" />


**2. System-Reaktion und Fehlermeldung (Nachher):

<img width="4000" height="3000" alt="1000052678" src="https://github.com/user-attachments/assets/9ac17abe-0e1b-4b69-bd0b-141841da36c2" />

