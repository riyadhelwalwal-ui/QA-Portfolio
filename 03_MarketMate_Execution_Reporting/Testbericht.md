# Hausaufgabe: Testdurchführung & Testberichterstattung (MarketMate)

## **1. Testdurchführungsbericht (Test Execution Log)**

**Testumgebung:**
- **Schnittstelle:** Web-Applikation ([https://masterschool.com](https://grocerymate.masterschool.com/))
- **Betriebssystem:** Windows 11 / Google Chrome
- **Tester:** Riyadh Elwalwal
- **Datum:** 21. Juli 2026

### **Ausführung der Testfälle (Basierend auf den 3 neuen Features)**

| Testfall-ID | Feature | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TF-01** | 1. Bewertungssystem | Sternebewertung und Textfeld sind auf der Produktdetailseite sichtbar. | Elemente sind sichtbar. | **PASS** |
| **TF-02** | 1. Bewertungssystem | Nur verifizierte Käufer können eine Bewertung abgeben. | System blockiert Nicht-Käufer korrekt mit Hinweistext. | **PASS** |
| **TF-03** | 1. Bewertungssystem | Das Textfeld erlaubt Kommentare bis maximal 500 Zeichen. | **System erlaubt gigantische Texte über 112.000 Zeichen.** | **FAIL** (Siehe Bug #03) |
| **TF-04** | 2. Altersverifikation | Ein Pop-up öffnet sich beim Aufruf der Kategorie „Alocohol“. | Pop-up erscheint fälschlicherweise direkt beim Shop-Aufruf. | **FAIL** (Siehe Bug #01) |
| **TF-05** | 2. Altersverifikation | Normale Produkte (Gemüse/Obst) sind ohne Altersprüfung zugänglich. | Gesamter Shop wird blockiert, bevor man normale Produkte sieht. | **FAIL** |
| **TF-06** | 3. Versandkosten | Versandkosten entfallen komplett ab exakt 50,00 € Einkaufswert. | System nutzt fälschlicherweise ein 20 € Limit im Text. | **FAIL** (Siehe Bug #02) |
| **TF-07** | 3. Versandkosten | Bei Werten unter 50,00 € wird eine Pauschale von 4,95 € erhoben. | Versandkosten bleiben immer bei 0 €, selbst unter 20 € (z.B. 9.13 €). | **FAIL** (Siehe Bug #02) |

---

## **2. Zusammenfassung der Testergebnisse (Summary)**

*   **Testfälle insgesamt:** 7
*   **Erfolgreich (Pass):** 2
*   **Fehlgeschlagen (Fail):** 5
*   **Gefundene Haupt-Bugs:** 3 kritische funktionale Fehler im System dokumentiert.
