# 📑 Testbericht: Versandkostenberechnung - Testfall 5 (Fehlerhafter Grenzwert bei 20 €)

### 🔗 Testfall-ID: MM-VK-02 (Kritischer Logikfehler beim Schwellenwert für kostenlosen Versand)

#### 🔗 1. Genaue Schritte zur Reproduktion des Fehlers (Schritt-für-Schritt):
1. Öffnen Sie die GroceryMate Webshop-Schnittstelle im Browser Chrome.
2. Überprüfen Sie die offizielle Spezifikation (Detaillierte Anforderung), die einen Gratisversand erst ab exakt **50,00 €** vorschreibt.
3. Suchen Sie nach dem Produkt "Cherries" auf der Startseite des Webshops.
4. Stellen Sie die Produktmenge im Eingabefeld auf exakt **8** ein, sodass der Produktwert genau **20,00 €** beträgt.
5. Klicken Sie auf das Warenkorb-Symbol und wechseln Sie zur Checkout-Seite (/checkout).
6. Kontrollieren Sie die berechneten Versandkosten in der Zeile "Shipment" sowie den blauen Hinweistext auf der UI.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Da der Einkaufswert von 20,00 € deutlich unter dem Spezifikationslimit von 50,00 € liegt, muss das System die feste Versandpauschale von 4,95 € berechnen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten / Fehlverhalten):
**[KRITISCHER LOGIK-BUG GEFUNDEN]:** Das System schaltet ab exakt **20,00 €** fälschlicherweise den kostenlosen Versand (**0 €**) frei. Dies steht im direkten Widerspruch zur detaillierten Anforderung (Gratisversand erst ab 50,00 €). Zudem wird auf der UI der fehlerhafte Text *"Free shipment if your purchase is 20€ or more."* angezeigt.

#### 🔗 4. Status: FAIL 🔴 (Kritischer Logik- und UI-Spezifikationsfehler dokumentiert)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)

**1. Offizielle Anforderung laut Spezifikation (Vorher):**  

<img width="1467" height="213" alt="Bildschirmfoto_13-8-2026_2297_github com" src="https://github.com/user-attachments/assets/e633003e-5801-4678-8ef9-d0ccb7509048" />



**2. Fehlerhafte Gratisversand-Anzeige bei exakt 20,00 € (Nachher):**
 
<img width="3000" height="4000" alt="1000052684" src="https://github.com/user-attachments/assets/689f10ec-1f64-4bf9-a0e7-b09343aef2f9" />
