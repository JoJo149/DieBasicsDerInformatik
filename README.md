# Einführung in die Informatik
Dies ist ein Testprojekt für meinen kleinen Bruder, mit dem Ziel ihm die Grundlagen der Informatik näherzubringen.
Dabei gehe ich auf die Grundlagen für Informatiker ein, welche sinnvoll sind schon vor Studienbeginn einmal gesehen zu haben.
Ich werde versuchen so viel wie möglich auf die jeweiligen Konstrukte einzugehen ohne dabei einen Anfänger, für welchen dies der erste Kontakt mit dem Mysterium der Informatik ist zu überfordern.

Dieses Tutorial/Einführung ist nur für Linux oder OSX (also Mac OS) user geschrieben und wird vielleicht, wenn ich die Zeit dazu finde für windows erweitert.

Dabei werden bestimmte Aufgaben vor allem am Anfang ein Terminal benötigen.
Ich werde so gut wie möglich versuchen beim Nutzen der Befehle diese auch zu erklären, bei Mac will ich noch erwähnen, dass es empfehlenswert ist [Iterm](https://iterm2.com/) zu nutzen.

## Start ?
Naja bevor wir mit irgendetwas starten müssen wir erst mal die Tools, welche man benötigt, um das Projekt auszuführen, installieren.\
Die Kurzfassung der benötigten Programme siehst du in der Liste von [Programmen](#dependencies), falls du schon weißt wie man mit Paketmanagern umgeht kannst du diese direkt installieren.
Im Folgenden werde ich auf die Nutzung von Paketmanagers und ähnlichem eingehen und deren Anwendung erklären.

### package management software
Stell dir einen App Store für programmierer vor, wobei alles Gratis ist und man anstatt Apps sogenannte Pakete installiert.
Diese Pakete können zwar auch Apps wie Firefox sein, können aber eben vor allem auch bestimmte Tools wie z.B. git sein, welche man zum Programmieren benötigt.
Ein Paketmanager ermöglicht also vereinfachtes Installieren, Aktualisieren und Deinstallieren von Programmen.\
Dabei ist wichtig zu erwähnen, dass die Pakete welche man installieren will auch beim jeweiligen Paketmanager vorliegen müssen.
Dadurch kann es schnell passieren, dass man mehrere paket manager für unterschiedliche Tools installiert hat.
Dabei würde ich dir empfehlen, in der Zukunft, wenn du jemals vor der Frage stehst, pro Programmiersprache nur einen einzigen paket manager zu nutzen.\
Da paket manager meist open source sind, genau wie die meisten Pakete darauf, ist es immer wichtig sicherzugehen von wem man was installiert.
Dabei musst du jetzt nicht direkt Angst haben, sondern du solltest einfach vor der Installation checken, ob jenes Tool bekannt ist und wer dieses Tool finanziert (was du so oder so machen solltest).\
Nun also zu der Entscheidung welchen Paketmanager du nutzen solltest.
Bei den meisten Linux Distros ist ein paket manager mit geliefert, falls du nicht weißt, welcher bei deinem Distro enthalten ist, solltest du Google mal fragen.
Bei Mac hingegen würde ich die Installation vom Paketmanager [homebrew](https://brew.sh/) stark empfehlen.

#### Wie installiere ich nun also Sachen mit meinem Paket Manager ?
Ich werde im Folgenden nun den Ablauf zum Installieren der benötigten Programme beschreiben, wobei ich nur die Befehle für Ubuntu und Mac OS direkt erwähne, der Ablauf sollte jedoch für die anderen Linux paket manager ähnlich sein.

Nun also zu unserer ersten Installation: Python\
Python nutzen wir für die Abgabetests, um zu überprüfen, dass du eine Python version installiert hast schreibe folgendes in dein Terminal:\
`python3 -V` \
Falls dies nicht etwas wie: `Python 3.13.2` Ausgibt ist das auch kein Problem.
Wir wollen nämlich eigentlich den paket manager für Python installieren `pip`, da python für diesen eine Voraussetzung ist installieren die meisten paket manager Python einfach direkt mit, wenn man pip installiert:
<div style="display: flex; gap: 20px;">
<div style="flex: 1;">
<strong>Für Ubuntu</strong>
<pre><code class="language-bash">
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
</code></pre>
</div>
<div style="flex: 1;">
<strong>Für Mac</strong>
<pre><code class="language-bash">
brew install python3
</code></pre>
</div>
</div>

Nachdem wir den paket manager für python installiert haben, wollen wir auch gleich ein Paket mit diesem Installieren:\
`pip install pytest`

Nun benötigen wir noch einen C-Compiler damit du auch die Aufgaben erledigen kannst.
Was genau das ist und wie man sowas benutzt lernst du in den Folgenden Aufageben noch.\
Wir nutzen als C-Compiler in diesem Beispiel gcc(GNU Compiler Collection):
<div style="display: flex; gap: 20px;">
<div style="flex: 1;">
<strong>Für Ubuntu</strong>
<pre><code class="language-bash">
sudo apt install build-essential
</code></pre>
</div>
<div style="flex: 1;">
<strong>Für Mac</strong>
<pre><code class="language-bash">
brew install gcc
</code></pre>
</div>
</div>

Merkst du schon, wie viel Zeit du durch die Nutzung eines paket managers einsparst?\
Nein ? Dann kannst du mal aus Spass, dich durch die unten verlinkte Installation vom C-Compiler durchklicken.

Nun zum letzten Tool welches du benötigst: git\
Git ist ein Versionierungungstool, wobei wir darauf in Aufgabe00 nochmal genauer eingehen werden.
<div style="display: flex; gap: 20px;">
<div style="flex: 1;">
<strong>Für Ubuntu</strong>
<pre><code class="language-bash">
sudo apt install git-all
</code></pre>
</div>
<div style="flex: 1;">
<strong>Für Mac</strong>
<pre><code class="language-bash">
brew install git
</code></pre>
</div>
</div>


### Dependencies

<details>
<summary>Klicke hier, um die Abhängigkeiten anzuzeigen</summary>

- [python](https://www.python.org/downloads/)
  - [pytest](https://pypi.org/project/pytest/)
- [C compiler](https://gcc.gnu.org/install/)
- [git](https://git-scm.com/downloads)

</details>


# Start !
Naja, fast haha. Wir müssen uns noch unser Projekt aus dem Internet auf die Festplatte holen.\
Dafür öffne erst einmal das Terminal und führe den Befehl `ls` aus.
Dieser Befehl bedeutet list und listet, wie der Name schon vermuten lässt, alle Ordner und Dateien in deinem aktuellen Ordner auf.
Jedes Unix basierte Dateisystem (also so gut wie alles ausser Windows) ist wie eine Wurzelstruktur aufgebaut, beginnend mit der sogenannten Root `/`.\
Als Nächstes solltest du versuchen in einen Ordner zu navigieren, in welchen du das Repository reinkopieren willst, hilfreiche Befehle dafür sind:
```bash
#list
ls
#change directory: also gehe in Ordner
cd <Ordnername>
#gehe in den nächst höheren (Parent) Ordner
cd ..
#make directory: erstelle einen Ordner
mkdir <Ordnername>
```

### Ein Repository klonen:
Mit dem Befehl ```git clone <repository-url>``` legst du eine lokale Kopie des Repository an.
Beim Aufruf des Befehls wirst du gegebenenfalls nach deinem Nutzeraccount gefragt.
Um den Accountnamen und das Password nicht immer eingeben zu müssen, kann der Zugang per SSH3 eingerichtet werden.
Nach dem Klonen findest du das Repository in dem dabei neu erstellten Ordner, checke dies mit `ls`.
Dort kannst du nun deine Abgabendateien versionieren und Branches verwalten.

### Nach dem Clonen:
Um das Projektsetup zu vollenden, musst du noch folgendes im Terminal ausführen:\
```chmod +x setup.bash```\
```./setup.bash```\
Stelle dabei sicher, dass du im Projektordner bist und wenn du `ls` Aufrufst die Datei `setup.bash` angezeigt wird.

Falls dies alles geklappt hat und das Programm keine Fehler ausgespuckt hat, bist du ready dich an `Aufgabe00` zu versuchen.