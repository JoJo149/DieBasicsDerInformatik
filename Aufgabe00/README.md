# Aufgabe 00 - NOT Ready

Diese Aufgabe beschäftigt sich mit den Basics von Git.
Für diese Aufgabe würde ich das Nutzen von einem Terminal sowie einem Texteditoren gegenüber einer IDE empfehlen.

## Arbeiten mit verteilten Repositories
Git ist ein freies verteiltes Versionsverwaltungssystem und kommt hauptsächlich bei der Entwicklung von Software zum Einsatz. Es protokolliert Änderungen an Dateien (z. B. Programmcode) in einem Repository und erlaubt dabei jederzeit Zugriff auf jeden der protokollierten Zustände (Commits). Änderungen am Programmcode sind somit immer nachvollziehbar. Softwareentwicklern ist es dadurch möglich, parallel und koordiniert an einem gemeinsamen Projekt zu arbeiten.

Mit dem Befehl ```git init``` kannst Du nun in diesem Verzeichnis ein lokales Repository initialisieren. Dabei wird ein Unterverzeichnis1 .git angelegt, welches das Grundgerüst des Repository beinhaltet. Die Dateien in diesem Unterverzeichnis werden durch Git selbst verwaltet und sollten im Regelfall nicht angepasst werden.
Der Status des Repository kann mit dem Befehl git status abgefragt werden. Dieser gibt unter anderem an, in welchem Branch Du Dich im Repository befindest. Für das eben erstellte Repository sollte das der master oder main-Branch sein. Ebenso zeigt der Status, ob geänderte Dateien im Repository sind. Da dieses Repository noch leer ist, werden keine Änderungen angezeigt.
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