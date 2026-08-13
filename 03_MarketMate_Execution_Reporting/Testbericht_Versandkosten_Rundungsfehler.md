# 📑 Testbericht: Versandkostenberechnung - Testfall 4 (Rundungsfehler bei Pauschale)

### 🔗 Testfall-ID: MM-VK-01 (Fehlerhafte Rundung der Versandpauschale unter 50,00 €)

#### 🔗 1. Genaue Schritte zur Reproduktion (Schritt-für-Schritt):
1. Öffnen Sie die GroceryMate Webshop-Schnittstelle im Browser Chrome.
2. Suchen Sie nach dem Produkt "Cherries" auf der Startseite.
3. Stellen Sie die Produktmenge im Eingabefeld auf exakt **1** ein (Produktwert beträgt 2,50 €).
4. Navigieren Sie zum Checkout (/checkout) und überprüfen Sie den Betrag in der Zeile "Shipment".

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Da der Einkaufswert unter 50,00 € liegt, muss das System die exakte Versandpauschale von **4,95 €** berechnen und auf der UI anzeigen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten / Fehlverhalten):
**[RUNDUNGS-BUG GEFUNDEN]:** Das System berechnet fälschlicherweise einen glatten Betrag von **5 €** für das Shipment. Es liegt ein Rundungsfehler im Code vor, der den exakten Spezifikationswert von 4,95 € ignoriert und den Endpreis fälschlicherweise erhöht.

#### 🔗 4. Status: FAIL 🔴 (Rundungsfehler in der Berechnungslogik erfasst)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)
<img width="3000" height="4000" alt="1000052683" src="https://github.com/user-attachments/assets/2c82b98c-4a32-45af-9ee1-6b549c3b780f" />


<!-- اسحب هنايا الصورة الثالثة اللي فيها حساب الكرز بـ 2.50 يورو والشحن 5 يورو -->


<!-- اسحب هنايا الصورة الثانية اللي فيها حساب الكرز بـ 20.00 يورو والشحن 0 يورو بالخطأ -->
