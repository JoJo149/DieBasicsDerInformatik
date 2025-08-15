# Aufgabe 01

Diese Aufgabe beschäftigt sich mit den Basics von Git, sowie einem einfachen Ausführen eines C-Programms.

## Arbeiten mit verteilten Repositories
### Verwalten von Branches
Mithilfe von Branches können verschiedene Entwicklungen parallel betrieben und später wieder zusammengefügt werden (Merge). In der Lehrveranstaltung nutzen wir Branches jedoch ausschließlich zur Trennung der einzelnen Abgaben. 
Ein neuer Branch wird immer vom letzten Commit (Zustand) des aktiven Branches abgezweigt. 
Mit dem Befehl ```git branch <branch-name>``` kann ein Branch erzeugt und mit ```git branch -d <branch-name>``` wieder gelöscht werden.
Eine Übersicht aller verfügbaren Branches erhält man mit ```git branch -a```.
Den jeweils aktiven Branch kann man mit dem Befehl ```git checkout <branch-name>``` wechseln.

Nun versuche einmal einfach den Inhalt von egal.txt an zu passen und diesen zu add, commiten und zu pushen.

## Aufgabe 01.1

Wie dir vielleicht aufgefallen ist, ist dies im Moment noch nicht möglich, zum pushen, musst du nämlich erst einmal die folgende Aufgabe Lösen:

