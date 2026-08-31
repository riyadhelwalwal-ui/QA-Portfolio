📑 Testbericht: Versandkostenberechnung - Testfall 6 (Grenzwertanalyse bei 30€ Warenwert)

### 🔗 Testfall-ID: MM-VK-02 (Erkennung des Fehlers bei der Versandkostenpauschale)

#### 🔗 1. Genaue Schritte zur Reproduktion/Ausführung im Testskript:
1. Öffnen Sie die GroceryMate-Webseite.
2. Klicken Sie auf das Profil-Symbol und loggen Sie sich mit den gültigen Testdaten ein.
3. Passieren Sie die Altersverifikation auf der Shop-Seite mit gültigen Daten (1987).
4. Erhöhen Sie die Anzahl der Gala Apples im Warenkorb um exakt "5" weitere Einheiten, sodass die Gesamtmenge im Feld auf 15 steigt (Warenwert = 30.00 €).
5. Klicken Sie auf „Add to Cart“ und wechseln Sie zur Checkout-Schnittstelle.
6. Überprüfen Sie die berechneten Versandkosten auf dem Bildschirm.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Da der Warenwert mit 30.00 € deutlich unter der kostenlosen Grenze von 50.00 € liegt, muss das System zwingend die Versandkostenpauschale von **4.95 €** aufschlagen und auf der UI anzeigen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten im automatisierten Test):
**[FEHLER IM SYSTEM GEFUNDEN - TEST FAILED 🔴]:** Das automatisierte Testskript hat einen kritischen AssertionError ausgelöst, da die Pauschale von 4.95 € nicht im Seitentext gefunden wurde. Das System berechnet fälschlicherweise 0.00 € Versandkosten bereits ab 20€/30€ Einkaufswert.

#### 🔗 4. Status: FAIL 🔴 (Spezifikationsfehler erfolgreich per Automation dokumentiert)
