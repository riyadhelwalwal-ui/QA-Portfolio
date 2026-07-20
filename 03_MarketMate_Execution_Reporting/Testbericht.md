# Hausaufgabe: Testdurchführung & Testberichterstattung (MarketMate)

## **1. Testdurchführungsbericht (Test Execution Log)**

**Testumgebung:**
- **Schnittstelle:** Web-Applikation (https://grocerymate.masterschool.com/)
- **Betriebssystem:** Windows 11 / Google Chrome
- **Tester:** Riyadh Elwalwal
- **Datum:** 20. Juli 2026

### **Ausführung der Testfälle (Basierend auf den 3 neuen Features)**

| Testfall-ID | Feature | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TF-01** | 1. Bewertungssystem | Sternebewertung und Textfeld sind auf der Produktdetailseite sichtbar. | Elemente sind sichtbar. | **PASS** |
| **TF-02** | 1. Bewertungssystem | Nur verifizierte Käufer können eine Bewertung abgeben. | System blockiert Nicht-Käufer korrekt mit Hinweistext. | **PASS** |
| **TF-03** | 2. Altersverifikation | Ein Pop-up öffnet sich beim Aufruf der Kategorie „Alocohol“. | Pop-up erscheint fälschlicherweise direkt beim Shop-Aufruf. | **FAIL** (Siehe Bug #01) |
| **TF-04** | 2. Altersverifikation | Normale Produkte (Gemüse/Obst) sind ohne Altersprüfung zugänglich. | Gesamter Shop wird blockiert, bevor man normale Produkte sieht. | **FAIL** |
| **TF-05** | 3. Versandkosten | Versandkosten entfallen komplett ab exakt 50,00 € Einkaufswert. | System nutzt fälschlicherweise ein 20 € Limit im Text. | **FAIL** (Siehe Bug #02) |
| **TF-06** | 3. Versandkosten | Bei Werten unter 50,00 € wird eine Pauschale von 4,95 € erhoben. | **Versandkosten bleiben immer bei 0 €, selbst bei Werten unter 20 € (z.B. 9.13 €).** | **FAIL** (Siehe Bug #02) |

---

## **2. Zusammenfassung der Testergebnisse (Summary)**

*   **Testfälle insgesamt:** 6
*   **Erfolgreich (Pass):** 2
*   **Fehlgeschlagen (Fail):** 4
*   **Gefundene Haupt-Bugs:** 2 kritische funktionale Fehler im System dokumentiert.

