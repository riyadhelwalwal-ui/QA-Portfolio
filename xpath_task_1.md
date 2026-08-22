# 📑 Hausaufgabe 1 - XPath Lösungen & HTML Dokumentation

## 🌐 1. Gegebenes HTML-Dokument (Referenz)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nested Complex HTML Document</title>
</head>
<body>
    <header>
        <h1 id="mainTitle">Welcome to Our Company</h1>
        <nav>
            <ul>
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About Us</a></li>
                <li>
                    <a href="#services" class="nav-link">Services</a>
                    <ul class="dropdown">
                        <li><a href="#webdev">Web Development</a></li>
                        <li><a href="#graphicdesign">Graphic Design</a></li>
                        <li><a href="#seo">SEO Services</a></li>
                    </ul>
                </li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h2 class="sectionTitle">About Us</h2>
            <div class="content">
                <p>We are a leading company in the industry.</p>
                <div class="team">
                    <h3>Our Team</h3>
                    <ul>
                        <li>
                            <h4>John Doe</h4>
                            <p>CEO</p>
                        </li>
                        <li>
                            <h4>Jane Smith</h4>
                            <p>CTO</p>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        <section id="services">
            <h2 class="sectionTitle">Our Services</h2>
            <div class="service-list">
                <div class="service-item">
                    <h3>Web Development</h3>
                    <p>Creating stunning websites.</p>
                </div>
                <div class="service-item">
                    <h3>Graphic Design</h3>
                    <p>Designing visual content.</p>
                </div>
                <div class="service-item">
                    <h3>SEO Services</h3>
                    <p>Improving search engine rankings.</p>
                </div>
            </div>
        </section>
        <section id="contact">
            <h2 class="sectionTitle">Contact Us</h2>
            <form id="contactForm">
                <label for="name">Name:</label>
                <input type="text" id="id" required>
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                <label for="message">Message:</label>
                <textarea id="message" placeholder="Your Message"></textarea>
                <input type="submit" value="Send Message">
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Company Name. All rights reserved.</p>
    </footer>
</body>
</html>
```

---

## 🛠️ 2. Aufgabenstellungen & Präzise XPath-Lösungen

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
