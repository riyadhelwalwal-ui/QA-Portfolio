# 📑 Hausaufgabe 1 - XPath Lösungen

Dieses Dokument enthält die präzisen XPath-Ausdrücke basierend auf dem bereitgestellten HTML-Dokument für **Aufgabe 1**. Alle Locators wurden nach den Best Practices für Robustheit und Selektivität erstellt.

---

### 🛠️ Lösungen für die Elemente 1 bis 15:

#### 1. Haupt-h1-Element finden:
* **XPath:** `//h1[@id='mainTitle']`
* **Beschreibung:** Findet das h1-Element direkt über seine eindeutige ID.

#### 2. Navigationslink "About Us" auswählen:
* **XPath:** `//nav//a[text()='About Us']`
* **Beschreibung:** Nutzt die fortgeschrittene `text()` Funktion, um den genauen Linktext im Navigationsbereich anzusteuern.

#### 3. Dropdown-Link "Graphic Design" auswählen:
* **XPath:** `//ul[@class='dropdown']//a[@href='#graphicdesign']`
* **Beschreibung:** Filtert gezielt innerhalb der Dropdown-Klasse nach dem spezifischen href-Attribut.

#### 4. Name des Teammitglieds "Jane Smith" auswählen:
* **XPath:** `//div[@class='team']//h4[text()='Jane Smith']`
* **Beschreibung:** Springt in den Team-Bereich und sucht nach dem exakten Namen im h4-Tag.

#### 5. Beschreibung der "SEO Services" (im Absatz) auswählen:
* **XPath:** `//div[@class='service-item'][h3[text()='SEO Services']]/p`
* **Beschreibung:** Findet das Service-Element über seine h3-Überschrift und wählt den direkt darunter liegenden Absatz (p) aus.

#### 6. Alle Service-Elemente im Abschnitt "Our Services" auswählen:
* **XPath:** `//section[@id='services']//div[@class='service-item']`
* **Beschreibung:** Gibt eine Liste aller Service-Elemente innerhalb der Services-Sektion zurück.

#### 7. E-Mail-Eingabefeld im Kontaktformular auswählen:
* **XPath:** `//form[@id='contactForm']//input[@id='email']`
* **Beschreibung:** Findet das Eingabefeld über die eindeutige ID innerhalb des spezifischen Formulars.

#### 8. Das gesamte Kontaktformular auswählen:
* **XPath:** `//form[@id='contactForm']`
* **Beschreibung:** Wählt den gesamten Formular-Container über seine ID aus.

#### 9. Das Footer-Absatz-Element auswählen:
* **XPath:** `//footer/p`
* **Beschreibung:** Direktes Ansteuern des Absatz-Elements innerhalb des Footers.

#### 10. Name (<h4>) des ersten Teammitglieds auswählen:
* **XPath:** `(//div[@class='team']//ul/li/h4)[1]`
* **Beschreibung:** Nutzt die Indexierung, um exakt das erste h4-Element in der Team-Liste zu isolieren.

#### 11. Beschreibung des zweiten Service-Elements auswählen:
* **XPath:** `(//section[@id='services']//div[@class='service-item']/p)[2]`
* **Beschreibung:** Nutzt die Indexierung, um den Beschreibungstext des zweiten Service-Eintrags auszuwählen.

#### 12. Überschrift der Sektion "Contact Us" (<h2>Element) auswählen:
* **XPath:** `//section[@id='contact']/h2[@class='sectionTitle']`
* **Beschreibung:** Steuert das h2-Element direkt über die übergeordnete Kontakt-Sektion an.

#### 13. Alle Links innerhalb des Dropdowns unter "Services" auswählen:
* **XPath:** `//ul[@class='dropdown']//li/a`
* **Beschreibung:** Wählt alle Ankertags (Links) aus, die sich innerhalb des Dropdown-Menüs befinden.

#### 14. Das erste `<li>` im Abschnitt "Our Team" auswählen:
* **XPath:** `(//div[@class='team']//ul/li)[1]`
* **Beschreibung:** Findet das exakt erste Listen-Element (li) im Organisationsbereich des Teams.

#### 15. Schaltfläche "Send Message" im Kontaktformular finden:
* **XPath:** `//form[@id='contactForm']//input[@type='submit']`
* **Beschreibung:** Identifiziert den Absende-Button über den Typ innerhalb des Kontaktformulars.
