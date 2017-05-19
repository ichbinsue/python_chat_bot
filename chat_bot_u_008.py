""" Diese Datei enthält den Anfang unseres Chat-bot-Programms und dient als
    gemeinsame Entwicklungsgrundlage.
    Sie ist unter Edmodo als "Chat_bot_(u/h)_yyy.py" gespeichert.
    Zum Ausführen einfach runterladen und in die Python IDE
    einfügen, danach den Code ausführen lassen. Oder in einen Texteditor
    kopieren und in deinem Python-Arbeitsverzeichnis als chat_bot.py 
    speichern und dort über Befehl: <python3 "Chat_bot_(u/h)_yyy.py"> ausführen lassen
    """
    
""" Mehrzeiliger Kommentar als Vorlage zum Kopieren
    """
# Einzeiliger Kommentar als Vorlage zum Kopieren
# --------------------------------------------------------------------------------
# Hier beginnt das eigentliche Programm
# -------------------------------------------------------------------------------- 
# Uwe meint der Bot müsse analog zum Menschen verschiedene Phasen eines Lebenszyklus
# kennen. Wachphasen in denen die Interaktionen mit dem Aussenwelt und 
# Schlafphasen in denen umfangreichere interne Datenreorganisation stattfinden.
# dazu gibt es eine erste äußere while-Schleife, die anzeigt, dass das Programm
# aktiv, also gestartet ist. (while s_live). Dazu muss s_live vorher initialisiert
# werden, wozu es einen Block (global definitions) gibt. Systemrelevante globale
# Variablen sollen durch ein (s_) kenntlich gemacht werden.
#           begin global definition 
s_live = True
# Die Systemvariable s_live wird auf True gesetzt. So lange diese Variable True ist
# wird die folgende Schleife abgearbeitet (Das entspricht dem äußeren Lebenszyklus
# des Bots)
s_zustand = 'wach'
# Die Systemvariable s_zustand wird auf ‘wach’ gesetzt. Dies bedeutet der Bot befindet
# sich im Interaktionsmodus
#           end global definition
#           begin main routine 
while s_live:
# Der Bot checkt ob er am Leben ist.
    while s_zustand == 'wach':
# Der Bot checkt ob er im Interaktionsmodus ist. 
# Interaktionsmodus heisst der Bot
# fragt seine Sensoren ab. Bislang bedeutet dies die Keyboardeingabe als Standard
# input und das Austauschverzeichnis für den Löbner-Prize-Turing-Test. Später
# könnten dies auch Kamera- Mikrofon- oder Signale von sonstigen Sensoren sein.
# Dazu muss er seinen Sinnen (Sensoren, Inputkanälen) 
# für gewisse Zeit Aufmerksamkeit zuwenden.
        eingabe = input('warte...')
# Hier wartet er auf eine Eingabe über die Tastatur,
# was natürlich sehr
# unbefriedigend ist wenn für die nächsten 24 Stunden keiner mit ihm über diesen 
# Kanal reden will. Hier muss eine Zeitsteuerung rein. z.B. 3 Sekunden auf Input
# warten, wenn nichts kommt auf dem nächsten Kanal für 3 Sekunden lauschen.
# Wenn was kommt weiterlauschen und kommunizieren bis max 3 Minuten nichts mehr 
# passiert, danach Kanal wechseln. Wenn 10 Minuten auf keinem Kanal was kommt,
# schlafen gehen.
        if eingabe == 'Hallo Jarvis' :
            print('Hallo, bin ',s_zustand)
        elif eingabe == 'stirb' :
            s_live = False
            s_zustand = 'tot'
        elif eingabe != '':
            print('Wie bitte?')
        else:
            s_zustand = 'schlafend'
    else:
# Ende der Interaktionsphase (Wachphase)
        while s_zustand == 'schlafend':
# Der Bot checkt ob er am Schlafen ist
# Hier soll der Bot jetzt seine langfristige Datenbasis reorganisieren und 
# entscheiden, ob er bei Input auf einem der Kanäle aufwachen will ode nicht.
            eingabe = input('chrchr...') 
            if eingabe == 'aufwachen' :
                s_zustand = 'wach'
                print('Uuuuuhaaaa')
            else:
                print('chrchr...',s_zustand)
        else:
# Der Bot hat im wachmodus den Befehl zum sterben (beenden des programms bekommen)
            print('Uff, bin',s_zustand)
else: print(s_live)
# Der Bot ist nicht mehr im Zustand lebend
#           end main routine            
