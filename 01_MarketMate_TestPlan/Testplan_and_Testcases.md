
# 1. Hausaufgabe: Testplan & Testfallentwurf

## Testobjekt (System unter Test):
**Webshop:** https://masterschool.com (MarketMate Homepage & Navigation)

---

## **1. Produktanalyse**

**Zielsetzung**
Das Ziel von MarketMate ist es, Kunden eine intuitive und visuell ansprechende E-Commerce-Plattform für den Online-Einkauf von frischen Lebensmitteln und Gemüse zu bieten. Die Homepage dient als zentraler Einstiegspunkt für die Produktsuche und Navigation.

**Zielnutzergruppe**
- Endkunden (B2C), die schnell und unkompliziert frische Lebensmittel online suchen, filtern und bestellen möchten.

**Hardware- und Software-Spezifikationen**
- **Hardware:** Desktop-PCs/Laptops (mind. 4 GB RAM) sowie gängige Smartphones/Tablets (iOS & Android) für das responsive Layout.
- **Software:** Aktuelle Browser-Versionen von Google Chrome, Mozilla Firefox, Apple Safari und Microsoft Edge.

**Funktionalität des Produkts (Fokus auf die 3 neuen Features auf der Homepage)**
1. **Push-Benachrichtigungen für Lagerbestand:** Ein System, das Kunden benachrichtigt (per E-Mail oder Pop-up), sobald ein ausverkauftes Produkt wieder auf Lager ist.
2. **Dark Mode Toggle:** Ein Button im Header, mit dem der Benutzer die UI-Farbe der Webseite von hell auf dunkel umschalten kann, um die Augen zu schonen.
3. **Favoriten-Funktion (Favorites List):** Die Möglichkeit, Produkte direkt auf der Homepage über ein Herz-Symbol auf eine Wunschliste zu setzen.

---

## **2. Teststrategie entwerfen**

**Testumfang (Scope of Testing)**
- **Im Umfang enthalten:** Funktion, UI-Darstellung und Performance der 3 neuen Komponenten (Push-Benachrichtigungen, Dark Mode, Favoriten-Interaktion) direkt auf der Homepage.
- **Nicht im Umfang enthalten:** Der eigentliche Bezahlvorgang (Checkout) oder die logistische Abwicklung im Backend.

**Geplante Testarten**
- **Funktionstests (Manuell):** Überprüfung der Klickwege und der korrekten Datenanzeige.
- **Regressionstests (Automatisiert):** Sicherstellen, dass die bestehende Navigation (Home, Shop, Contact) fehlerfrei bleibt.
- **Usability-Tests:** Validierung der Barrierefreiheit und Responsivität der Banners und Menüs auf mobilen Geräten.

---

## **3. Testziele definieren**

**Ziele**
- **Funktionalität:** Alle drei neuen Komponenten reagieren exakt nach Spezifikation und ohne spürbare Verzögerung.
- **GUI-Konsistenz:** Alle neuen Icons (Herz, Mond-Symbol) fügen sich nahtlos in das blaue Corporate Design ein.

**Erwartete Ergebnisse**
- Das Aktivieren des Dark Modes ändert das CSS-Theme fehlerfrei.
- Das Herz-Icon im Header aktualisiert die Anzahl der hinzugefügten Produkte synchron.

---

## **4. Testkriterien definieren**

**Aussetzungskriterien (Suspension Criteria)**
- Die obere Navigationsleiste (Header) wird nicht geladen oder ist komplett verschoben.
- Produkte auf der Homepage werden nicht gerendert (leere Seite).

**Abnahmekriterien (Exit Criteria)**
- Mindestens 95% aller geschriebenen Testfälle erfolgreich durchlaufen.
- Keine offenen kritischen UI-Bugs oder funktionale Fehler im Such- und Favoriten-System.

---

## **5. Ressourcenplanung**
- **Personal:** 1 QA-Engineer (Manuell & Automatisierung).
- **Infrastruktur:** TEST-Umgebung des Webshops, Zugriff auf GitHub Repository.

---

## **6. Planung der Testumgebung**
Die Tests laufen in der **TEST-Umgebung**. Validierung der UI-Responsivität (Responsive Design) für die Banner ("Delicious Salad Everyday", "Fresh Vegetables") mittels Chrome Developer Tools und echten Test-Smartphones.

---

## **7. Zeitplan und Aufwandsschätzung**
- **Testplanung & Design:** 1.5 Tage (6 Stunden)
- **Manuelle Testdurchführung:** 1 Tag (4 Stunden)
- **Testautomatisierung:** 2 Tage (10 Stunden)

---

## **8. Testliefergegenstände (Test-Deliverables)**
- Aktualisiertes Testplandokument.
- Testfallsammlung (siehe unten).
- Test-Exit-Bericht.

---
---

# Testfallentwurf (Test Case Design)

### **Feature 1: Push-Benachrichtigungen für Lagerbestand**

| Testfall ID | Beschreibung / Schritt | Erwartetes Ergebnis | Testentwurfs-Technik | Automatisierbar? (Ja/Nein) + Warum |
| :--- | :--- | :--- | :--- | :--- |
| **TF-01** | Klick auf „Benachrichtigen, wenn verfügbar“ bei einem ausverkauften Produkt. | Ein Pop-up bestätigt, dass der Benutzer benachrichtigt wird, sobald das Produkt wieder auf Lager ist. | Äquivalenzklassenbildung | **Ja.** Das Erscheinen des Pop-ups und der API-Status lassen sich automatisiert abgreifen. |
| **TF-02** | Erneuter Klick auf den Button (Abbestellen der Benachrichtigung). | Die Benachrichtigung wird erfolgreich storniert und der Button-Text ändert sich wieder. | Äquivalenzklassenbildung | **Ja.** Wichtig für die Regression, um Datenmüll in der Datenbank zu vermeiden. |
| **TF-03** | Klick auf den Button ohne im System eingeloggt zu sein. | Das System leitet den Benutzer direkt zur Login-Seite weiter. | Error Guessing | **Ja.** Ein klassischer Sicherheits- und Logiktest für die User Journey. |

### **Feature 2: Dark Mode Toggle **

| Testfall ID | Beschreibung / Schritt | Erwartetes Ergebnis | Testentwurfs-Technik | Automatisierbar? (Ja/Nein) + Warum |
| :--- | :--- | :--- | :--- | :--- |
| **TF-04** | Klick auf das neue Mond-Symbol im Header der Homepage. | Der Hintergrund der Webseite wechselt sofort von Weiß auf Dunkelgrau/Schwarz (CSS-Klassenänderung). | Äquivalenzklassenbildung | **Ja.** Automatisierte Tests können prüfen, ob das HTML-Attribut (z.B. `data-theme="dark"`) korrekt gesetzt wird. |
| **TF-05** | Erneuter Klick auf das Symbol (Wechsel zurück zum Light Mode). | Die Webseite wechselt sofort wieder in das standardmäßige helle Design zurück. | Äquivalenzklassenbildung | **Ja.** Einfacher UI-Zustandstest, der perfekt in die automatisierte Pipeline passt. |
| **TF-06** | Aktivieren des Dark Modes, Schließen des Browser-Tabs und erneutes Öffnen der Homepage. | Der Dark Mode bleibt aktiv (Einstellung wurde im LocalStorage des Browsers gespeichert). | Error Guessing | **Nein.** Die korrekte visuelle Darstellung und das Nicht-Flackern der Farben beim Laden testet man initial manuell. |

### **Feature 3: Favoriten-Funktion (Favorites List)**

| Testfall ID | Beschreibung / Schritt | Erwartetes Ergebnis | Testentwurfs-Technik | Automatisierbar? (Ja/Nein) + Warum |
| :--- | :--- | :--- | :--- | :--- |
| **TF-07** | Klick auf das neue Herz-Symbol bei einem Produkt (z. B. Orangen) auf der Homepage. | Das Herz-Icon wird farblich ausgefüllt und der Favoriten-Zähler in der oberen Navbar erhöht sich um 1. | Äquivalenzklassenbildung | **Ja.** Statustests von Icons und Zählern sind essenziell für automatisierte Funktionstests. |
| **TF-08** | Klick auf das bereits aktivierte Herz-Icon (Entfernen aus Favoriten). | Das Herz wird wieder leer und der Zähler im Header verringert sich synchron um 1. | Grenzwertanalyse | **Ja.** Sichert ab, dass der Zähler nicht unter Null sinkt oder falsch rechnet. |
| **TF-09** | Klick auf „Favorites“ im Header, um die Favoritenliste zu öffnen. | Die Liste öffnet sich und zeigt exakt die Produkte an, die zuvor auf der Homepage markiert wurden. | Äquivalenzklassenbildung | **Nein.** Das visuelle Grid-Layout der Favoritenseite und das Laden der Produktbilder werden manuell verifiziert. |
