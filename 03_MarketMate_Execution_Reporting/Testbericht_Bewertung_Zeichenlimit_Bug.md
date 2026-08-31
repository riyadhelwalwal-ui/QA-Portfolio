📑 Testbericht: Bewertungssystem - Testfall 8 (Grenzwertvalidierung bei 500 Zeichen)

### 🔗 Testfall-ID: MM-BW-02 (Erfolgreiche UI-Validierung des Feedback-Zeichenlimits)

#### 🔗 1. Genaue Schritte zur Reproduktion/Ausführung:
1. Öffnen Sie die GroceryMate-Webseite.
2. Klicken Sie auf das Profil-Symbol und loggen Sie sich mit den gültigen Testdaten ein.
3. Klicken Sie auf die Schaltfläche „Shop“.
4. Geben Sie im Pop-up-Fenster zur Altersverifikation das Geburtsdatum ein und klicken Sie auf „Confirm“.
5. Fügen Sie ein Produkt (Gala Apples) in den Warenkorb und schließen Sie den Kaufprozess im Checkout ab (Dummy-Daten-Eingabe).
6. Nach der automatischen Weiterleitung zur Homepage klicken Sie erneut auf das gekaufte Produkt (Gala Apples), um die Detailseite zu öffnen.
7. Scrollen Sie nach unten zum Bewertungssystem ("What is your view?").
8. Kopieren Sie einen generierten Testtext mit einer Länge von exakt 600 Zeichen und fügen Sie diesen in das Textfeld ein.

#### 🔗 2. Erwartetes Ergebnis (Soll-Verhalten laut Spezifikation):
Das System muss die Eingabe im Textfeld bei exakt 500 Zeichen blockieren, den Counter auf "500/500" setzen und das Weiterschreiben oder Einfügen weiterer Zeichen im UI-Feld unmöglich machen.

#### 🔗 3. Tatsächliches Ergebnis (Ist-Verhalten):
**[UI-VALIDIERUNG ERFOLGREICH]:** Das System verhält sich spezifikationsgemäß im Frontend. Der Text wird bei exakt 500 Zeichen abgeschnitten. Der rote UI-Counter zeigt "500/500" an und blockiert erfolgreich jeden weiteren Text. Zudem erscheint die korrekte rote Warnmeldung "You cannot tell us more about this product.".

#### 🔗 4. Status: PASSED 🟢 (Soll- und Ist-Verhalten stimmen auf UI-Ebene exakt überein)
