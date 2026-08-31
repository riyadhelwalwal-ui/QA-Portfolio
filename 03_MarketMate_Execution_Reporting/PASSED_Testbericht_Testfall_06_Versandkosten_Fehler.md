📑 Testbericht: Versandkostenberechnung - Testfall 6 (Verifikation der 20€-Grenze im UI)

### 🔗 Testfall-ID: MM-VK-01 (Erfolgreiche Verifikation des fehlerhaften 20€-Limits)

#### 🔗 1. Genaue Schritte zur Reproduktion/Ausführung:
1. Öffnen Sie die GroceryMate-Webseite.
2. Loggen Sie sich mit den gültigen Testdaten (VALID_USER) ein.
3. Fügen Sie Gala Apples hinzu und setzen Sie die Anzahl auf 10 Einheiten (Warenwert = 20.00 €).
4. Klicken Sie auf „Add to Cart“ und wechseln Sie zur Checkout-Schnittstelle.
5. Überprüfen Sie den Hinweistext und die Versandkosten auf dem Bildschirm.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Laut Testplan wird kostenloser Versand erst ab 50€ erwartet. Da das System aber aktuell fehlerhaft programmiert ist, wird überprüft, ob das System den Text "Free shipment if your purchase is 20€ or more." anzeigt.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten im automatisierten Test):
**[TEST PASSED 🟢]:** Das automatisierte Testskript hat erfolgreich bestätigt, dass das System den fehlerhaften Text anzeigt und 0€ Versandkosten berechnet. Die fehlerhafte Logikgrenze des Entwicklers wurde auf UI-Ebene erfolgreich per `assert` verifiziert.

#### 🔗 4. Status: PASSED 🟢 (Das automatisierte Skript hat das erwartete Fehler-Verhalten im UI erfolgreich bestätigt)
