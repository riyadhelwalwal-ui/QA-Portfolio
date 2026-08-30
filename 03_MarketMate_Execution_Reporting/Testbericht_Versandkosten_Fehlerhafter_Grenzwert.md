📑 Testbericht: Versandkostenberechnung - Testfall 5 (Fehlerhafter Grenzwert bei 20 €)

### 🔗 Testfall-ID: MM-VK-02 (Kritischer Logikfehler beim Schwellenwert für kostenlosen Versand)

#### 🔗 1. Genaue Schritte (Ausführungsschritte):
1. Öffnen Sie die MarketMate-Homepage.
2. Klicken Sie oben im Header auf das Benutzer-Profil-Symbol (Account Icon) und loggen Sie sich mit den gültigen Testdaten ein.
3. Klicken Sie auf die Schaltfläche „Shop“, um zu den Produkten zu gelangen.
4. Geben Sie im nun erscheinenden Pop-up-Fenster zur Altersverifikation das Geburtsdatum ein und klicken Sie auf „Confirm“.
5. Suchen Sie auf der ersten Seite nach dem Produkt "Gala Apples" (Preis: 2€).
6. Stellen Sie die Produktmenge im Eingabefeld auf exakt 10 ein, sodass der Gesamtwert genau 20,00 € beträgt.
7. Klicken Sie auf „Add to Cart“, um die Produkte in den Warenkorb zu legen.
8. Wechseln Sie zur Checkout-Seite (/checkout) und kontrollieren Sie die berechneten Versandkosten in der Zeile "Shipment".

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Da der Einkaufswert von 20,00 € deutlich unter dem gesetzten Spezifikationslimit von 50,00 € liegt, muss das System die feste Versandpauschale von 4,95 € berechnen und anzeigen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten / Fehlverhalten):
**[KRITISCHER LOGIK-BUG GEFUNDEN]:** Das System schaltet ab exakt 20,00 € fälschlicherweise den kostenlosen Versand (0 €) frei. Dies steht im direkten Widerspruch zur detaillierten Anforderung (Gratisversand erst ab 50,00 €). Zudem wird auf der UI der fehlerhafte Text "Free shipment if your purchase is 20€ or more." angezeigt.

#### 🔗 4. Status: FAIL 🔴 (Kritischer Logik- und UI-Spezifikationsfehler dokumentiert)

<img width="862" height="437" alt="Screenshot 2026-08-31 000056" src="https://github.com/user-attachments/assets/2b06340b-2780-4e55-bc2c-83e1ab2a1bb0" />

