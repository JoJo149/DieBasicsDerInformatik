# Aufgabe 01

Diese Aufgabe beschäftigt sich mit den Basics von Git, sowie einem einfachen Ausführen eines C-Programms.
Für diese Aufgabe würde ich das Nutzen von einem Terminal sowie einem Texteditoren gegenüber einer IDE empfehlen.

## Arbeiten mit verteilten Repositories
### Verwalten von Branches
Mithilfe von Branches können verschiedene Entwicklungen parallel betrieben und später wieder zusammengefügt werden (Merge). In der Lehrveranstaltung nutzen wir Branches jedoch ausschließlich zur Trennung der einzelnen Abgaben. 
Ein neuer Branch wird immer vom letzten Commit (Zustand) des aktiven Branches abgezweigt. 
Mit dem Befehl ```git branch <branch-name>``` kann ein Branch erzeugt und mit ```git branch -d <branch-name>``` wieder gelöscht werden.
Eine Übersicht aller verfügbaren Branches erhält man mit ```git branch -a```.
Den jeweils aktiven Branch kann man mit dem Befehl ```git checkout <branch-name>``` wechseln.

Nun versuche einmal einfach den Inhalt von egal.txt an zu passen und diesen zu adden, zu commiten und zu pushen.

## Aufgabe 01.1

Falls du alles richtig gemacht hast, hast du gerade eine Fehlermeldung bekommen.
Um dies zu Beheben musst du dein gelerntes Wissen nun Anwenden:

- Stelle sicher, dass Du Dich im master oder main-Branch Deines Repository befindest (```git status```)
- Erstelle einen neuen Branch mit dem Namen: ```local-branch```
- Wechsel in den neuen Branch
- Erstelle nun die Datei```test.txt``` im Ordner von Aufgabe01 und verändere sie, wie du willst.
- adde die Datei, erzeuge einen Commit und lasse dir das Commit-Log ausgeben (```git log```).
- Wechsel zurück in den master oder main-Branch. Lasse Dir das Commit-Log ausgeben und vergleiche es mit der vorherigen Ausgabe

## Aufgabe 01.2

Schreibe ein C-Programm, welches auf dem Terminal mittels printf den Text ```Hallo, <Name>!``` ausgibt.\
Die Ausgabe soll auf einer separaten Zeile erfolgen.\
Eine beispielhafte Benutzung des Programms liefe ab wie in Listing 1 gezeigt:\
Listing 1: Kompilieren und Aufruf des Programms
```
> clang -std=c11 -Wall -g solution.c -o solution
> ./solution
Hallo , Jonas!
```

Gehe sicher, dass Deine Aufgabe dabei die folgenden Bedingungen erfüllt:
- Die Ein- und Ausgabebibliothek stdio.h wird geladen.
- Die Funktion main ist definiert.
- printf wird zur Ausgabe von Text benutzt.
- kein White Space am Anfang oder Ende oder zwischen der neuen Zeile und !

Die Datei kompiliert ohne Fehler und Warnungen beim Aufruf von:\
```clang -std=c11 -Wall -g solution.c -o solution```