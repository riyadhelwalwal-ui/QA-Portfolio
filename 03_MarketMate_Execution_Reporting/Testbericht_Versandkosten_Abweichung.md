# 📑 Testbericht: Versandkostenberechnung - Testfall 4 (Abweichung der Versandpauschale)

### 🔗 Testfall-ID: MM-VK-01 (Unerwarteter Betrag der Versandpauschale unter 50,00 €)

#### 🔗 1. Genaue Schritte zur Reproduktion (Schritt-für-Schritt):
1. Öffnen Sie die GroceryMate Webshop-Schnittstelle im Browser Chrome.
2. Suchen Sie nach dem Produkt "Cherries" auf der Startseite.
3. Stellen Sie die Produktmenge im Eingabefeld auf exakt **1** ein (Produktwert beträgt 2,50 €).
4. Navigieren Sie zur Checkout-Seite (/checkout) und kontrollieren Sie den Betrag in der Zeile "Shipment".

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Da der Einkaufswert unter 50,00 € liegt, muss das System die exakte Versandpauschale von **4,95 €** berechnen und auf der Benutzeroberfläche anzeigen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[FEHLER IM PREISSYSTEM GEFUNDEN]:** Das System zeigt auf der UI einen Betrag von **5 €** für das Shipment an. Es liegt eine Abweichung vom Spezifikationswert vor, wodurch der Endpreis für den Kunden fälschlicherweise erhöht wird. *(Mögliche Ursache: Rundungsfehler bei der Float-Konvertierung im Code).*

#### 🔗 4. Status: FAIL 🔴 (Abweichung in der Preisberechnung dokumentiert)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)

<img width="3000" height="4000" alt="1000052683" src="https://github.com/user-attachments/assets/2c82b98c-4a32-45af-9ee1-6b549c3b780f" />

