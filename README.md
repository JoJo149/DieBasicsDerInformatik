# Einführung in die Informatik
Dies ist ein Testprojekt für meinen kleinen Bruder, mit dem Ziel ihm die Grundlagen der Informatik näherzubringen.

# Dependencies

- python
  - pytest
- C compiler
- git 

# Setup

Um das Projekt setup fertig zu machen folgendes im Terminal laufen:\
```chmod +x setup.bash```\
```./setup.bash```

# Aufgabe 00
### Erste Schritte mit Git
Git ist ein freies verteiltes Versionsverwaltungssystem und kommt hauptsächlich bei der Entwicklung von Software zum Einsatz. Es protokolliert Änderungen an Dateien (z. B. Programmcode) in einem Repository und erlaubt dabei jederzeit Zugriff auf jeden der protokollierten Zustände (Commits). Änderungen am Programmcode sind somit immer nachvollziehbar. Softwareentwicklern ist es dadurch möglich, parallel und koordiniert an einem gemeinsamen Projekt zu arbeiten.

### Initialisieren eines Git-Repository
Erstelle ein Verzeichnis mit beliebigem Namen ```mkdir <name>``` und wechsel in dieses Verzeichnis ```cd <name>```. Mit dem Befehl ```git init``` kannst Du nun in diesem Verzeichnis ein lokales Repository initialisieren. Dabei wird ein Unterverzeichnis1 .git angelegt, welches das Grundgerüst des Repository beinhaltet. Die Dateien in diesem Unterverzeichnis werden durch Git selbst verwaltet und sollten im Regelfall nicht angepasst werden.
Der Status des Repository kann mit dem Befehl git status abgefragt werden. Dieser gibt unter anderem an, in welchem Branch Du Dich im Repository befindest. Für das eben erstellte Repository sollte das der master oder main-Branch sein. Ebenso zeigt der Status, ob geänderte Dateien im Repository sind. Da dieses Repository noch leer ist, werden keine Änderungen angezeigt.

### Ein Repository klonen:
Mit dem Befehl ```git clone <repository-url>``` legst Du eine lokale Kopie des Repository an. Beim Aufruf des Befehls wirst Du gegebenenfalls nach Deinem Nutzeraccount gefragt. Um den Accountnamen und das Password nicht immer eingeben zu müssen, kann der Zugang per SSH3 eingerichtet werden. Nach dem Klonen findest Du das Repository in dem dabei neu erstellten Ordner. Dort kannst Du nun Deine Abgabendateien versionieren und Branches verwalten.

## Nach dem Clonen des Repositories kannst du dich nun an Aufgabe01 versuchen.
