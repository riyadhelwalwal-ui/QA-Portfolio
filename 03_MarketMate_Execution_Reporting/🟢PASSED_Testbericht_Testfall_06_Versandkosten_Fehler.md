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
<img width="911" height="414" alt="Screenshot 2026-09-01 001740" src="https://github.com/user-attachments/assets/e137fa13-f2e6-4cd5-b100-bd61ec2ba425" />
<img width="953" height="472" alt="Screenshot 2026-09-01 001004" src="https://github.com/user-attachments/assets/04267d7d-097b-4ba8-89a9-b72c82e2f37a" />
