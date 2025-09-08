# Aufgabe 00

Diese Aufgabe beschäftigt sich mit den Basics von Git.
Für diese Aufgabe würde ich das Nutzen von einem Terminal ohne die Nutzung eine IDE empfehlen.

## ein kleiner Git-Guide

> **Hinweis vorneweg:**  
> Git ist nicht nur ein Tool. Git ist ein Lifestyle. Und zwar einer, bei dem du dich regelmäßig selbst verfluchst, weil du deine Branches verhunzt hast. Aber keine Sorge — wir gehen das zusammen durch.

Git ist ein freies verteiltes Versionsverwaltungssystem und der weltweite Standard für Softwareprojekten.
Also kurz gesagt das Tool, mit dem sich jeder Entwickler wenigstens ein wenig auskennen sollte.

## 1. Dein erstes Repo

Du hast einen Ordner mit Code und willst, dass Git sich drum kümmert.

```console
git init
```

Zack. Jetzt wohnt in .git/ ein kleines Monster, das alles mitbekommt, was du tust. Löschen, umbenennen, um drei Uhr nachts committen — es sieht alles.

## 2. Dateien hinzufügen
```console
git add mein_code.py
git add .
```
`git add .` heißt: „Ich will, dass Git sich an ALLES hier erinnert.“\
Pro-Tipp: Mach das nicht blind. Sonst landet auch deine geheime pw.txt im Repo.
Schreibe dir lieber ein umfangreiches [`.gitignore`](../.gitignore) wie in diesem Repository um die ganzen unnötigen extra files nicht zu adden.

## 3. Committen
```console
git commit -m "Mein erster Commit"
```
Ein Commit ist ein Schnappschuss. Denk an ein Savegame in deinem Lieblingsspiel.
Und wie beim Savegame: wenn du keins machst, darfst du beim nächsten Crash wieder von vorne anfangen.

## 4. Status-Check
```console
git status
```
Dein bester Freund. Git sagt dir:
- „Hey, diese Datei kenn ich nicht.“
- „Die da wurde geändert.“
- „Alles sauber, ab nach Hause.“

## 5. Branches
Ein Branch ist einfach ein Paralleluniversum deiner Arbeit.
```console
git branch feature-x
git checkout feature-x
```
Boom. Jetzt bist du im neuen Universum. Dein Code kann dort alles kaputt machen, ohne dass main was davon merkt.
Perfekt also, falls man mit mehreren Leuten gleichzeitig an einem Projekt arbeitet.\
Pro-Tipp: Der Befehl `git checkout -b feature-x` erzeugt und besucht den Branch sofort.\
Debugging-Tipp: Du kannst auch `git checkout alten_commit` nutzen um einen früheren Projektzustand zu checken.

## 6. Zusammenführen (Merge)
Irgendwann willst du deine Parallelwelt zurück in die Hauptwelt schieben:
```console
git checkout main
git merge feature-x
```
Wenn Git brav ist: alles klappt.\
Wenn Git zickt: Merge-Konflikt. Willkommen in der Hölle. Aber hey, wenigstens bist du nicht allein.

## Arbeiten mit verteilten Repositories
Es protokolliert Änderungen an Dateien (z. B. Programmcode) in einem Repository und erlaubt dabei jederzeit Zugriff auf jeden der protokollierten Zustände (Commits). Änderungen am Programmcode sind somit immer nachvollziehbar. Softwareentwicklern ist es dadurch möglich, parallel und koordiniert an einem gemeinsamen Projekt zu arbeiten.

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