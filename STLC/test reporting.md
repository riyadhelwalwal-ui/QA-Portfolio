# 📑 STLC: Test Execution & Reporting

## 🔴 1. Testbericht: Versandkostenberechnung - Testfall 06 (Grenzwertanalyse bei 30€ Warenwert)

| Schritt | Action / Testschritt | Erwartetes Ergebnis (Soll) | Tatsächliches Ergebnis (Ist) | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | GroceryMate-Webseite öffnen & einloggen. | Erfolgreicher Login auf der Plattform. | Login erfolgreich durchgeführt. | **OK** |
| **2** | Altersverifikation passieren (1987). | Pop-up schließt, Shop wird freigegeben. | Pop-up erfolgreich geschlossen. | **OK** |
| **3** | Apples-Menge auf 15 erhöhen (Warenwert = 30.00 €). | Menge wird im UI auf 15 gesetzt. | Menge erfolgreich auf 15 gesetzt. | **OK** |
| **4** | „Add to Cart“ klicken und zum Checkout wechseln. | Checkout-Seite öffnet sich. | Checkout-Seite erfolgreich geöffnet. | **OK** |
| **5** | Versandkosten im Checkout überprüfen. | Pauschale von **4.95 €** wird berechnet. | **[BUG]:** System berechnet fälschlicherweise **0.00 €**. | **NOT OK** |

### 🤖 Automatisierter Nachweis (PyTest):
* **Status:** **FAILED 🔴 (Bug per Automation dokumentiert)**
* **Fehlermeldung:** `AssertionError: assert '4.95' in browser.page_source`

---

## 🔴 2. Testbericht: Altersverifikation - Testfall 01 (Fehlerhafte Altersberechnung)

| Schritt | Action / Testschritt | Erwartetes Ergebnis (Soll) | Tatsächliches Ergebnis (Ist) | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | GroceryMate-Webseite öffnen & einloggen. | Erfolgreicher Login auf der Plattform. | Login erfolgreich durchgeführt. | **OK** |
| **2** | Im Pop-up das Geburtsdatum „01.05.1987“ eingeben. | System berechnet das Alter korrekt als über 18. | System speichert das Datum erfolgreich. | **OK** |
| **3** | Auf die Schaltfläche „Confirm“ klicken. | Pop-up schließt, Zugriff wird erlaubt. | **[BUG]:** UI zeigt Fehlermeldung "You are underage" an. | **NOT OK** |
| **4** | Versuchen, Kategorie „Alkoholische Getränke“ zu öffnen. | Kategorie wird komplett freigegeben. | Zugriff bleibt fälschlicherweise gesperrt. | **NOT OK** |

### 🤖 Automatisierter Nachweis (PyTest):
* **Status:** **FAILED 🔴 (Bug per Automation dokumentiert)**
* **Fehlermeldung:** `AssertionError: assert 'You are underage' not in browser.page_source`

