#Nachbarschafts-App Sicherheit
zaehler = 3 # die Variable zählt die Anmeldungsversuche

print("Willkommen in der Nachbarschaft!") 
input("Wie lautet ihr Name? ")
input("Bitte geben Sie eine Email adresse an: ")
        
while zaehler > 0 :  
    zugangscode = input("Bitte geben Sie ihren Zugangscode ein: ")
    if zugangscode == "NaNeu1234": # vergleichsoperator
        print("Sie haben sich erfolgreich angemeldet! Sie können jetzt auf den Nachbarschafts kalender, die Hilfsbörse und die Leih- und Tauschbörse zugreifen.")
        zaehler = -1 # änderung der varialbe
        
    else:
        print("Sie haben noch " +str(zaehler - 1)+  " Versuch/e.") # anzeige der anzahl der Versuche 
        zaehler = zaehler -1 # änderung der varialbe
    
if zaehler == 0 : # beendet die versuche
    print("Sie haben die Anzahl der Versuche überschritten, bitte versuchen Sie es später erneut")
    zaehler = zaehler +3 # änderung der variable
    
