# 📑 Hausaufgabe 1 - XPath Lösungen & Dokumentation

Dieses Dokument enthält die Aufgabenstellungen und die dazugehörigen präzisen XPath-Ausdrücke basierend auf dem bereitgestellten HTML-Dokument für **Aufgabe 1**.

---

## 🛠️ Aufgaben & XPath-Lösungen:

### 1. Schreibe das XPath, um das Haupt-h1 Element zu finden.
* **XPath:** `//h1[@id='mainTitle']`

### 2. Schreibe das XPath, um den Navigationslink About Us auszuwählen.
* **XPath:** `//nav//a[text()='About Us']`

### 3. Schreibe das XPath, um den Dropdown-Link Graphic Design auszuwählen.
* **XPath:** `//ul[@class='dropdown']//a[@href='#graphicdesign']`

### 4. Schreibe das XPath, um den Namen des Teammitglieds Jane Smith auszuwählen.
* **XPath:** `//div[@class='team']//h4[text()='Jane Smith']`

### 5. Schreibe das XPath, um die Beschreibung (die sich im Absatz befindet) der SEO Services auszuwählen.
* **XPath:** `//div[@class='service-item'][h3[text()='SEO Services']]/p`

### 6. Schreibe einen XPath-Ausdruck, um alle Service-Elemente im Abschnitt "Our Services" auszuwählen.
* **XPath:** `//section[@id='services']//div[@class='service-item']`

### 7. Wie lautet das XPath, um das E-Mail-Eingabefeld im Kontaktformular auszuwählen?
* **XPath:** `//form[@id='contactForm']//input[@id='email']`

### 8. Wie würdest du ein XPath schreiben, um das gesamte Kontaktformular auszuwählen?
* **XPath:** `//form[@id='contactForm']`

### 9. Gib das XPath an, um das Footer-Absatz-Element auszuwählen.
* **XPath:** `//footer/p`

### 10. Was ist das XPath, um den Namen (<h4>) des ersten Teammitglieds auswählen?
* **XPath:** `(//div[@class='team']//ul/li/h4)[1]`

### 11. Wie kannst du mit XPath die Beschreibung des zweiten Service-Elements auswählen?
* **XPath:** `(//section[@id='services']//div[@class='service-item']/p)[2]`

### 12. Was ist das XPath, um die Überschrift der Sektion "Contact Us" (<h2>Element) auszuwählen?
* **XPath:** `//section[@id='contact']/h2[@class='sectionTitle']`

### 13. Schreibe einen XPath-Ausdruck, um alle Links innerhalb des Dropdowns unter dem Navigationspunkt "Services" auszuwählen.
* **XPath:** `//ul[@class='dropdown']//li/a`

### 14. Was ist das XPath, um das erste <li> im Abschnitt "Our Team" auszuwählen?
* **XPath:** `(//div[@class='team']//ul/li)[1]`

### 15. Gib das XPath an, um die Schaltfläche "Send Message" im Kontaktformular zu finden.
* **XPath:** `//form[@id='contactForm']//input[@type='submit']`
