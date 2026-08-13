# 📑 Testbericht: Bewertungssystem - Testfall 8 (Grenzwertüberschreitung Textfeedback)

### 🔗 Testfall-ID: MM-BW-02 (Kritischer Validierungsfehler beim Zeichenlimit des Feedbacks)

#### 🔗 1. Genaue Schritte zur Reproduktion des Fehlers (Schritt-für-Schritt):
1. Öffnen Sie die GroceryMate Webshop-Schnittstelle im Browser Chrome.
2. Navigieren Sie zur Produktseite von "Oranges" und scrollen Sie nach unten zum Bereich des Bewertungssystems.
3. Analysieren Sie die bestehende Nutzerbewertung des Benutzers `abhisakh_3` bezüglich der Textlänge.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Das System darf Textfeedbacks mit einer Länge von **maximal 500 Zeichen** akzeptieren. Jede Eingabe, die diesen Grenzwert überschreitet, muss vom System blockiert oder abgeschnitten werden.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten / Fehlverhalten):
**[KRITISCHER VALIDIERUNGS-BUG GEFUNDEN]:** Das System besitzt keine clientseitige oder serverseitige Validierung der Textlänge. Der Benutzer `mimoeksh_3` konnte ein Textfeedback mit mehreren tausend Zeichen erfolgreich absenden und auf der UI veröffentlichen, was das gesamte Seitenlayout zerstört.

#### 🔗 4. Status: FAIL 🔴 (Kritischer Fehler bei Grenzwertvalidierung dokumentiert)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)

<img width="855" height="1740" alt="Bildschirmfoto_13-8-2026_3331_grocerymate masterschool com" src="https://github.com/user-attachments/assets/392be784-4b53-4fdf-ae5d-b3806e38872e" />
