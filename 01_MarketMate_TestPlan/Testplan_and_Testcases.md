# 📑 Testplan: MarketMate Webshop

---

## 1. Produktanalyse

### **Zielsetzung**
* Erweiterung des MarketMate Webshops um **3 neue Funktionen**.
* Sicherung der Stabilität der bestehenden Basisfunktionen (**Regression**).

### **Unterstützte Systeme**
* **Hardware & Software:** PCs, Laptops, Smartphones / Windows, macOS, Android, iOS.
* **Unterstützte Browser:** Google Chrome, Mozilla Firefox, Safari, Microsoft Edge.

---

## 2. Funktionalitäten (Features)

### **A. Bestehende Basisfunktionen**
* Registrierung und Login.
* Produktsuche mit Sortierfunktion und Kategorisierung.
* Warenkorb-Logik und Bestellabschluss (Checkout).

### **B. Neue Kernfeatures (Die 3 Anforderungen)**
1. **Bewertungssystem:** 5-Sterne-System + Textfeedback (max. 500 Zeichen). Nur für eingeloggte und verifizierte Käufer aktiv. Live-Aktualisierung der Gesamtnote.
2. **Altersverifikation:** Pop-up-Sperrfenster bei der Kategorie „Alkoholische Getränke“. Eingabe des Geburtsdatums ist Pflicht. Zugriff ab 18 Jahren, darunter erfolgt eine Fehlermeldung und Weiterleitung zur Startseite.
3. **Versandkostenberechnung:** Kostenloser Versand ab exakt 50,00 € Einkaufswert. Bei Werten darunter gilt eine Pauschale von 4,95 €. Der aktuelle Versandpreis wird im Warenkorb live angezeigt.

---

## 3. Teststrategie

### **Testumfang (Scope)**
* **In-Scope:** Logik von Alter (18+), Versandkosten (50€ Grenze) und Bewertungssystem (Zulassung & max. 500 Zeichen). Live-UI-Anzeigen im Checkout.
* **Out-of-Scope:** Externe Zahlungsschnittstellen (z.B. PayPal-Anbindung selbst) und Backend-Datenbankleistung ohne direkten UI-Einfluss.

### **Testarten**
* **Funktionstests (Functional Testing):** Prüfung der logischen Geschäftsregeln (Alter, Versand, Sterne).
* **Grenzwertanalyse (Boundary Value Analysis):** Validierung kritischer Werte (exakt 18 Jahre alt, 49,99 € vs. 50,00 €).

---

## 4. Testziele & Kriterien

### **Hauptziele**
* Alle 3 neuen Features funktionieren exakt wie spezifiziert.
* Keine Rundungs- oder Rechenfehler bei der Versandkostenberechnung im Checkout.
* Richtige UI-Fehlermeldungen bei Blockaden (Minderjährige, Nicht-Käufer).

### **Aussetzungskriterien**
* Kritische Fehler, die das Testen blockieren (z. B. Absturz des Alters-Pop-ups, wodurch der gesamte Webshop blockiert wird).

### **Abnahmekriterien (Exit Criteria)**
* Mindestens **9 Testfälle** (3 pro Feature laut Vorgabe) wurden dokumentiert und ausgeführt.
* Alle gefundenen Bugs wurden in den **GitHub Issues** erfasst.
* Einreichung des Testberichts inklusive visueller Nachweise (Screenshots).

---

## 5. Ressourcen und Testumgebung

* **Tester:** Riyadh Elwalwal (QA Engineer).
* **Tools:** Google Chrome Browser, PyCharm IDE, PyTest Framework, GitHub Issues.
* **Testumgebung:** Offizielle Live-Test-Schnittstelle (GroceryMate Webshop).
