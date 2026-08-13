# 📑 Testbericht: Versandkostenberechnung - Testfall 6 (Verifikation ab 50,00 €)

### 🔗 Testfall-ID: MM-VK-03 (Prüfung des kostenlosen Versands über dem Spezifikationslimit)

#### 🔗 1. Genaue Schritte zur Verifikation (Schritt-für-Schritt):
1. Öffnen Sie die GroceryMate Webshop-Schnittstelle im Browser Chrome.
2. Suchen Sie nach dem Produkt "Cherries" auf der Startseite.
3. Erhöhen Sie die Produktmenge im Eingabefeld auf exakt **21** (Produktwert beträgt genau 52,50 €, was über dem Limit von 50,00 € liegt).
4. Navigieren Sie zur Checkout-Seite (/checkout).
5. Überprüfen Sie den Betrag in der Zeile "Shipment".

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Ab einem Einkaufswert von exakt 50,00 € oder mehr müssen die Versandkosten auf 0,00 € (Kostenloser Versand) gesetzt und auf der UI angezeigt werden.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
Das System zeigt die Versandkosten korrekt als **0 €** an. Bei einem Warenwert von 52,50 € bleibt das Shipment bei 0 € und der Endbetrag (Total) beläuft sich auf 52,50 €. (Hinweis: Das erwartete Ergebnis für diesen spezifischen Grenzwert wird formal erfüllt, obwohl der zuvor dokumentierte Logik-Fehler den Gratisversand bereits ab 20 € fälschlicherweise freischaltet).

#### 🔗 4. Status: PASS 🟢 (Erwartetes Soll-Verhalten für Werte über 50,00 € formal erfüllt)

#### 🔗 5. Anhang: Nachweis (Visueller Beleg)

**1. Offizielle Anforderung laut Spezifikation (Vorher):**
 <img width="1467" height="213" alt="Bildschirmfoto_13-8-2026_2297_github com" src="https://github.com/user-attachments/assets/cdb25f54-81fa-440e-8ec3-f42959eaacfb" />


**2. Erfolgreicher kostenloser Versand bei über 50,00 € (Nachher):**
    <img width="3000" height="4000" alt="1000052685" src="https://github.com/user-attachments/assets/7473791b-6879-4e1f-9867-f5869b307e35" />

