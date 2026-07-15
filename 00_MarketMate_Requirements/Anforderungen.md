# 1. Hausaufgabe: Anforderungen & Feature-Analyse

## **Bestehende Funktionalitäten (MarketMate)**
- Registrierungs- und Login-Funktionalität
- Produktsuche mit Sortierfunktion (z. B. nach Preis) und Kategorisierung von Produkten
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabschluss (Checkout): Eingabe von Rechnungs- und Versandinformationen, Auswahl der Zahlungsmethode, Preisberechnung (Gesamtsumme)

---

## **Neue Features (Analyse nach Beispiel-Vorlage)**

### **1. Bewertungssystem für Produkte**

**Unklare Anforderung**:
- Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Fragen**:
1. Müssen sowohl die Sternebewertung als auch das schriftliche Feedback zwingend ausgefüllt werden, oder kann eine Bewertung auch ohne Text abgegeben werden?
2. Dürfen alle registrierten Nutzer jedes Produkt bewerten, oder ist die Funktion auf verifizierte Käufer (Kunden, die das Produkt tatsächlich bestellt haben) beschränkt?
3. Gibt es ein Zeichenlimit (Min/Max) für das schriftliche Feedback und wie wird das System gegen Spam oder schädliche Skripte (XSS) geschützt?
4. Wo genau auf der Produktdetailseite wird das Bewertungssystem und die Summe der bisherigen Bewertungen platziert?

**Detaillierte Anforderung**:
- Eingeloggte und verifizierte Käufer können auf der Produktdetailseite eine Bewertung abgeben. Das System bietet ein interaktives 5-Sterne-Auswahlfeld (Pflichtfeld) und ein optionales Textfeld für schriftliches Feedback (maximal 500 Zeichen). Das System validiert die Eingabe gegen Spam und schädliche Skripte. Nach dem Absenden wird die Gesamtdurchschnittsnote des Produkts im Katalog live aktualisiert.

---

### **2. Altersverifikation für alkoholische Produkte**

**Unklare Anforderung**:
- Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

**Fragen**:
1. Wie genau soll die Altersverifikation im Fenster erfolgen? (z. B. einfache Bestätigung per Button „Ich bin 18+“ oder durch Eingabe des Geburtsdatums?)
2. Wie lange bleibt der Verifikationsstatus gültig? Muss der Nutzer sein Alter bei jeder neuen Session bestätigen oder wird dies im Benutzerprofil/Cookie dauerhaft gespeichert?
3. Was passiert, wenn ein nicht-verifizierter Nutzer versucht, über einen direkten Link (URL-Bypass) auf ein alkoholisches Produkt zuzugreifen?
4. Welche Fehlermeldung oder Weiterleitung erfolgt, wenn der Nutzer angibt, unter 18 Jahre alt zu sein?

**Detaillierte Anforderung**:
- Beim ersten Aufrufen der Kategorie „Alkoholische Getränke“ innerhalb einer active Session öffnet sich ein modales Sperrfenster (Pop-up). Der Nutzer muss sein Geburtsdatum eingeben. Das System prüft, ob der Nutzer mindestens 18 Jahre alt ist. Wenn ja, wird der Zugriff freigeschaltet und der Status in einem Session-Cookie gespeichert. Wenn nein, wird der Zugriff verweigert, eine rote Fehlermeldung angezeigt und der Nutzer auf die Startseite zurückgeleitet. Ein direkter Zugriff per URL wird ohne aktives Cookie blockiert.

---

### **3. Änderungen bei den Versandkosten**

**Unklare Anforderung**:
- Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

**Fragen**:
1. Wie hoch ist der exakte Schwellenwert (Bestellwert in Euro), ab dem die Versandkosten entfallen?
2. Wie hoch sind die Standardversandkosten, wenn der Schwellenwert nicht erreicht wird?
3. Wird dem Kunden im Warenkorb dynamisch angezeigt, wie viel Euro ihm noch fehlen, um den kostenlosen Versand zu erreichen?
4. Wie verhält sich das System, wenn durch den Einsatz eines Rabattcodes der Gesamtwert der Bestellung nachträglich unter den Schwellenwert fällt?

**Detaillierte Anforderung**:
- Ab einem Bruttowarenwert von exakt 50,00 € entfallen die Versandkosten für den Kunden komplett. Liegt der Warenkorbwert darunter, wird eine pauschale Versandgebühr von 4,95 € erhoben. Das System berechnet die Versandkosten im Warenkorb und im Checkout dynamisch in Echtzeit. Im Warenkorb wird dem Nutzer ein Hinweistext angezeigt (z. B. „Noch 12,00 € bis zum kostenlosen Versand“). Wenn ein Rabattcode den Wert unter 50,00 € drückt, werden die Versandkosten automatisch wieder hinzugerechnet.
