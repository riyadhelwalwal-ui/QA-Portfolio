# Hausaufgabe: Testdurchführung & Testberichterstattung (MarketMate)

## **1. Testdurchführungsbericht (Test Execution Log)**

**Testumgebung:**
- **Schnittstelle:** Web-Applikation ((https://grocerymate.masterschool.com/))
- **Betriebssystem:** Windows 11 / Google Chrome
- **Tester:** Riyadh Elwalwal
- **Datum:** 22. Juli 2026

### **Ausführung der Testfälle (9 Testfälle - 3 pro Feature laut Vorgabe)**

| Testfall-ID | Feature | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status | Anhang (Screenshot) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TF-01** | 1. Bewertungssystem | Sternebewertung und Textfeld sind auf der Produktdetailseite sichtbar. | Elemente sind sichtbar. | **PASS** | [Siehe Anhang unten] |
| **TF-02** | 1. Bewertungssystem | Nur Nutzer mit verifizierter Kaufhistorie können eine Bewertung abgeben. | Das System blockiert unverifizierte Nutzer korrekt durch einen Hinweistext. | **PASS** | [Siehe Anhang unten] |
| **TF-03** | 1. Bewertungssystem | Das Textfeld erlaubt Kommentare bis maximal 500 Zeichen. | System erlaubt gigantische Texte über 112.000 Zeichen (abhisakh_3). | **FAIL** (Bug #03) | [Siehe Bug #03] |
| **TF-04** | 2. Altersverifikation | Ein Pop-up öffnet sich beim Aufruf der Kategorie „Alocohol“. | Pop-up erscheint fälschlicherweise direkt beim Shop-Aufruf. | **FAIL** (Bug #01) | [Siehe Bug #01] |
| **TF-05** | 2. Altersverifikation | Nutzer über 18 Jahre erhalten uneingeschränkten Zugriff auf Alkoholprodukte. | System berechnet das Alter falsch und blockiert Erwachsene (1980/1987). | **FAIL** (Bug #04) | [Siehe Bug #04] |
| **TF-06** | 2. Altersverifikation | Normale Produkte (Gemüse/Obst) sind auch für gesperrte Nutzer zugänglich. | System erlaubt korrekt das Browsen und Einkaufen von normalen Produkten. | **PASS** | [Siehe Anhang unten] |
| **TF-07** | 3. Versandkosten | Versandkosten entfallen komplett ab exakt 50,00 € Einkaufswert. | System nutzt fälschlicherweise ein 20 € Limit im Text. | **FAIL** (Bug #02) | [Siehe Bug #02] |
| **TF-08** | 3. Versandkosten | Bei Werten unter 50,00 € wird eine Pauschale von 4,95 € erhoben. | Versandkosten bleiben immer bei 0 €, selbst unter 20 € (z.B. 9.13 €). | **FAIL** (Bug #02) | [Siehe Bug #02] |
| **TF-09** | 3. Versandkosten | Der Warenkorb berechnet den Gesamtpreis der Produkte korrekt. | System berechnet Summen korrekt (z.B. 30.18 € und 9.13 € verifiziert). | **PASS** | [Siehe Anhang unten] |

---

## **2. Zusammenfassung der Testergebnisse (Summary)**

*   **Testfälle insgesamt:** 9
*   **Erfolgreich (Pass):** 3
*   **Fehlgeschlagen (Fail):** 6

---

## **3. Anhang: Nachweise für erfolgreiche Testfälle (PASS-Nachweise)**

### **Nachweis für TF-06 (Erfolgreiches Browsen im Shop trotz Underage-Status):**
<img width="3000" height="4000" alt="1000050622" src="https://github.com/user-attachments/assets/980d7b3a-d807-49be-9488-8f0f3552b35c" />
