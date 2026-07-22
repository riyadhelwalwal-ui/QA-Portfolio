# Hausaufgabe: Testdurchführung & Testberichterstattung (MarketMate)

## **1. Testdurchführungsbericht (Test Execution Log)**

**Testumgebung:**
- **Schnittstelle:** Web-Applikation https://grocerymate.masterschool.com/
- **Betriebssystem:** Windows 11 / Google Chrome
- **Tester:** Riyadh Elwalwal
- **Datum:** 22. Juli 2026

### **Ausführung der Testfälle (9 Testfälle - 3 pro Feature laut Vorgabe)**

| Testfall-ID | Feature | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status | Anhang (Screenshot) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TF-01** | 1. Bewertungssystem | Sternebewertung und Textfeld sind auf der Produktdetailseite sichtbar. | Elemente sind sichtbar. | **PASS** | [Screenshot_TF01.png] |
| **TF-02** | 1. Bewertungssystem | Nur verifizierte Käufer können eine Bewertung abgeben. | System blockiert Nicht-Käufer korrekt mit Hinweistext. | **PASS** | [Screenshot_TF02.png] |
| **TF-03** | 1. Bewertungssystem | Das Textfeld erlaubt Kommentare bis maximal 500 Zeichen. | System erlaubt gigantische Texte über 112.000 Zeichen (abhisakh_3). | **FAIL** (Bug #03) | [Screenshot_Bug03.png] |
| **TF-04** | 2. Altersverifikation | Ein Pop-up öffnet sich beim Aufruf der Kategorie „Alocohol“. | Pop-up erscheint fälschlicherweise direkt beim Shop-Aufruf. | **FAIL** (Bug #01) | [Screenshot_Bug01.png] |
| **TF-05** | 2. Altersverifikation | Nutzer über 18 Jahre erhalten uneingeschränkten Zugriff auf Alkoholprodukte. | **System berechnet das Alter falsch und blockiert Erwachsene trotz legitmer Eingabe (z.B. 1980/1987).** | **FAIL** (Bug #04) | [Screenshot_Age_Error.png] |
| **TF-06** | 2. Altersverifikation | Normale Produkte (Gemüse/Obst) sind auch für gesperrte Nutzer zugänglich. | System erlaubt korrekt das Browsen und Einkaufen von normalen Produkten. | **PASS** | [Screenshot_Celery_Notice.png] |
| **TF-07** | 3. Versandkosten | Versandkosten entfallen komplett ab exakt 50,00 € Einkaufswert. | System nutzt fälschlicherweise ein 20 € Limit im Text. | **FAIL** (Bug #02) | [Screenshot_Bug02.png] |
| **TF-08** | 3. Versandkosten | Bei Werten unter 50,00 € wird eine Pauschale von 4,95 € erhoben. | Versandkosten bleiben immer bei 0 €, selbst unter 20 € (z.B. 9.13 €). | **FAIL** (Bug #02) | [Screenshot_Bug02.png] |
| **TF-09** | 3. Versandkosten | Der Warenkorb berechnet den Gesamtpreis der Produkte korrekt. | System berechnet Summen korrekt (z.B. 30.18 € und 9.13 € verifiziert). | **PASS** | [Screenshot_TF09.png] |

---

## **2. Zusammenfassung der Testergebnisse (Summary)**

*   **Testfälle insgesamt:** 9
*   **Erfolgreich (Pass):** 3
*   **Fehlgeschlagen (Fail):** 6
*   **Gefundene Haupt-Bugs:** 4 funktionale Fehler im System dokumentiert.
