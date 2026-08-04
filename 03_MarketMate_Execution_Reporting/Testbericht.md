# Hausaufgabe: Testdurchführung & Testberichterstattung (MarketMate)
# 📑 Testbericht: Altersverifikation & Browsing-Logik

## **Testfall-ID: TF-06 (Erfolgreiches Browsen trotz Blockade)**

### **1. Genaue Schritte:**
1. Öffne die MarketMate-Homepage.
2. Klicke auf den Button "Shop".
3. Gib das Geburtsdatum "01.05.1987" im Pop-up ein und klicke auf "Bestätigen".
4. Navigiere zu normalen Produkten (Celery / Ginger) und füge sie in den Warenkorb hinzu.

### **2. Erwartetes Ergebnis:**
Das System berechnet das Alter korrekt (39 Jahre), schließt das Pop-up und erlaubt das fehlerfreie Browsen und Einkaufen von normalen Lebensmitteln.

### **3. Tatsächliches Ergebnis:**
Das System berechnet das Alter fälschlicherweise als minderjährig ("You are underage") und sperrt Alkohol, aber es erlaubt korrekt das Durchsuchen und Einkaufen von normalen Produkten (Celery/Ginger).

### **4. Status:** **PASS**

---

## **2. Anhang: Nachweis (Visual Evidence)**


## **3. Anhang: Nachweise für erfolgreiche Testfälle (PASS-Nachweise)**

### **Nachweis für TF-06 (Erfolgreiches Browsen im Shop trotz Underage-Status):**
<img width="3000" height="4000" alt="1000050622" src="https://github.com/user-attachments/assets/980d7b3a-d807-49be-9488-8f0f3552b35c" />
