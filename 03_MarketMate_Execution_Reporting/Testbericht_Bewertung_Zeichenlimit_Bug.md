# 📑 Testbericht: Bewertungssystem - Testfall 8 (Grenzwertüberschreitung Textfeedback)

### 🔗 Testfall-ID: MM-BW-02 (Fehler beim Zeichenlimit des Feedbacks)

#### 🔗 1. Genaue Schritte zur Reproduktion des Fehlers (Schritt-für-Schritt):
1. Öffnen Sie die GroceryMate Webshop-Schnittstelle im Browser Chrome.
2. Navigieren Sie zur Produktseite von "Oranges" und scrollen Sie nach unten zum Bereich des Bewertungssystems.
3. Analysieren Sie die bestehende Nutzerbewertung des Benutzers `abhisakh_3` bezüglich der Textlänge.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Das System darf Textfeedbacks mit einer Länge von **maximal 500 Zeichen** akzeptieren. Jede Eingabe, die diesen Grenzwert überschreitet, muss blockiert werden.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[FEHLER IM SYSTEM GEFUNDEN]:** Das System hat das Zeichenlimit von maximal 500 Zeichen ignoriert. Der Benutzer `abhisakh_3` konnte einen Text mit mehreren tausend Zeichen erfolgreich absenden, was das Layout der Webseite komplett verzerrt.

#### 🔗 4. Status: FAIL 🔴 (Fehler bei Grenzwertvalidierung dokumentiert)


#### 🔗 5. Anhang: Nachweis (Visueller Beleg)

<img width="855" height="1740" alt="Bildschirmfoto_13-8-2026_3331_grocerymate masterschool com" src="https://github.com/user-attachments/assets/392be784-4b53-4fdf-ae5d-b3806e38872e" />
