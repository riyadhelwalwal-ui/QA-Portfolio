# 📑 Testbericht: Bewertungssystem - Testfall 7 (Zugriffskontrolle für Nicht-Käufer)

### 🔗 Testfall-ID: MM-BW-01 (Verifikation der Sperrung des Bewertungssystems für Nicht-Käufer)

#### 🔗 1. Genaue Schritte zur Verifikation (Schritt-für-Schritt):
1. Öffnen Sie den GroceryMate Webshop im Browser Chrome und loggen Sie sich ein.
2. Navigieren Sie zu einem Produkt, das Sie zuvor **nicht gekauft** haben (z. B. "Oranges").
3. Scrollen Sie nach unten zum Bereich des Bewertungssystems.
4. Überprüfen Sie, ob die Sterne-Auswahl und das Textfeld zur Eingabe sichtbar oder blockiert sind.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Das System darf das Bewertungssystem nur für verifizierte Käufer freischalten. Für Nicht-Käufer muss das System gesperrt sein und einen entsprechenden Hinweis anzeigen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
Das System verhält sich korrekt wie spezifiziert. Die Sterne und das Textfeld sind komplett ausgeblendet. Es erscheint der graue UI-Hinweistext: `"You need to buy this product to tell us your opinion!"`. Der Zugriff wird erfolgreich blockiert.

#### 🔗 4. Status: PASS 🟢 (Sicherheits- und Zugriffskontrolle erfolgreich verifiziert)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)
<img width="1122" height="832" alt="Bildschirmfoto_13-8-2026_3153_grocerymate masterschool com" src="https://github.com/user-attachments/assets/a18d22de-763b-43b0-98e0-e740f86e7dfa" />
