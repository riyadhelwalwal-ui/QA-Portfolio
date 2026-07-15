# 1. Hausaufgabe: Anforderungen & Feature-Analyse (MarketMate)

## **Bestehende Funktionalitäten (MarketMate)**
- Registrierungs- und Login-Funktionalität
- Produktsuche mit Sortierfunktion und Kategorisierung von Produkten
- Produkte zu Favoriten hinzufügen und in den Warenkorb legen
- Bestellabschluss (Checkout)

---

## **Neue Features**

### **1. Bewertungssystem für Produkte**

**Unklare Anforderung**:
- Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Fragen**:
1. Muss man unbedingt Sterne auswählen, um einen Text zu schreiben, oder geht das auch ohne Sterne?
2. Darf jeder Besucher eine Bewertung schreiben, oder muss man dafür eingeloggt sein?
3. Wie viele Zeichen darf der Text maximal haben?

**Detaillierte Anforderung**:
- Eingeloggte Nutzer können auf der Produktseite eine Bewertung abgeben. Die Sterneauswahl ist freiwillig (kein Pflichtfeld). Das Textfeld für den Kommentar erlaubt maximal 500 Zeichen. Nach dem Absenden wird die Gesamtnote live aktualisiert.

---

### **2. Altersverifikation für alkoholische Produkte**

**Unklare Anforderung**:
- Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

**Fragen**:
1. Müssen die Nutzer ihr Geburtsdatum eintippen oder reicht ein einfacher Klick auf einen Button "Ich bin 18"?
2. Muss man das Alter bei jedem Besuch der Kategorie neu eingeben?
3. Was passiert, wenn ein Nutzer angibt, dass er unter 18 Jahre alt zu sein?

**Detaillierte Anforderung**:
- Wenn ein Nutzer die Kategorie „Alkoholische Getränke“ öffnet, erscheint ein Sperrfenster (Pop-up). Der Nutzer muss sein Geburtsdatum eingeben. Wenn er 18 oder älter ist, öffnet sich die Seite. Wenn er unter 18 ist, zeigt das System eine Fehlermeldung und leitet ihn zurück auf die Startseite.

---

### **3. Änderungen bei den Versandkosten**

**Unklare Anforderung**:
- Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

**Fragen**:
1. Ab wie viel Euro genau ist der Versand kostenlos?
2. Wie hoch sind die Versandkosten, wenn man diesen Betrag nicht erreicht?
3. Sieht der Kunde im Warenkorb live, wie viel Geld ihm noch für den kostenlosen Versand fehlt?

**Detaillierte Anforderung**:
- Ab einem Einkaufswert von exakt 50,00 € ist der Versand komplett kostenlos. Wenn der Wert darunter liegt, zahlt der Kunde eine Pauschale von 4,95 €. Der aktuelle Versandpreis wird im Warenkorb immer live angezeigt.
