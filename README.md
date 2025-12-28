# Einführung in die Informatik
Dies ist ein Testprojekt für meinen kleinen Bruder, mit dem Ziel ihm die Grundlagen der Informatik näherzubringen.
Dabei gehe ich auf die Grundlagen für Informatiker ein, welche sinnvoll sind schon vor Studienbeginn einmal gesehen zu haben.
Ich werde versuchen so viel wie möglich auf die jeweiligen Konstrukte einzugehen ohne dabei einen Anfänger, für welchen dies der erste Kontakt mit dem Mysterium der Informatik ist zu überfordern.

Dieses Tutorial/Einführung ist nur für Linux oder OSX (also Mac OS) user geschrieben und wird vielleicht, wenn ich die Zeit dazu finde für windows erweitert.

Dabei werden bestimmte Aufgaben vor allem am Anfang ein Terminal benötigen.
Ich werde so gut wie möglich versuchen beim Nutzen der Befehle diese auch zu erklären, bei Mac will ich noch erwähnen, dass es empfehlenswert ist [Iterm](https://iterm2.com/) zu nutzen.

Falls dies deine erste Nutzung von einem **Terminal** ist, kannst du dieses [cheatsheet](https://images.velog.io/images/hy9202/post/8f1f2c7e-4edf-49ec-9c9e-380ade1325a8/command-line-cheat-sheet-large01.png) als lookup table nutzen.

Es ist empfehlenswert für die ersten Aufgaben, einen **Texteditor im Terminal** zu nutzen, statt direkt eine große IDE wie CLion. Warum? Weil IDEs oft Features wie aggressive Autocompletion übernehmen – das kann für den Einstieg praktisch sein, aber man lernt dann nicht, wirklich selbst auf eine Lösung zu kommen und zu verstehen, was passiert.

### Empfehlungen für Texteditoren:
- **[Micro](https://micro-editor.github.io/)** – Texteditor, der sich gut mit der Maus bedienen lässt und klassische Tastenkürzel wie `Ctrl+S` unterstützt.
- **[Helix](https://helix-editor.com/)** – moderner Terminal-Editor, der schon viele nützliche Funktionen bietet und ein Neovim ähnliche Tastenbelegung nutzt.
- **[Neovim](https://neovim.io/)** – super anpassbar, mächtig, aber es kann am Anfang ein wenig überwältigend sein. Gut als Übung, um sich mit der eigenen Entwicklungsumgebung vertraut zu machen.

> Tipp: Wie schon erwähnt lohnt es sich für die ersten Aufgaben, einen schlanken Editor zu nutzen. Später, wenn Projekte größer werden oder du in C++ arbeitest, kann eine IDE wie Clion das Leben deutlich einfacher machen. Dann kannst du dich auf das konzentrieren, was wirklich Spaß macht: **Code schreiben und Programme entwickeln**, statt dich mit Konfigurationen oder fehlenden Features herumzuschlagen.


## Start ?
Na ja bevor wir mit irgendetwas starten müssen wir erst mal die Tools, welche man benötigt, um das Projekt auszuführen, installieren.\

Die Kurzfassung der benötigten Programme siehst du in der Liste von [Programmen](#dependencies), falls du schon weißt, wie man mit Paketmanagern umgeht und was sie sind, kannst du diese direkt installieren.

Im Folgenden werde ich auf die Nutzung von Paketmanagers und ähnlichem eingehen und deren Anwendung erklären.

### package management software
Stell dir einen App Store für programmierer vor, wobei alles Gratis ist und man anstatt Apps sogenannte Pakete installiert.
Diese Pakete können zwar auch Apps wie Firefox sein, können aber eben vor allem auch bestimmte Tools wie z.B. git oder gcc sein, welche man zum Programmieren benötigt.
Ein Paketmanager ermöglicht vereinfachtes Installieren, Aktualisieren und Deinstallieren von Programmen.\
Dabei ist wichtig zu erwähnen, dass die Pakete welche man installieren will auch beim jeweiligen Paketmanager vorliegen müssen.
Dadurch kann es schnell passieren, dass man mehrere paket manager für unterschiedliche Tools installiert hat.
Dabei würde ich dir empfehlen, pro Programmiersprache nur einen einzigen paket manager zu nutzen.\
Da paket manager meist open source sind, genau wie die meisten Pakete darauf, ist es immer wichtig sicherzugehen von wem man was installiert.
Dabei musst du jetzt nicht direkt Angst haben, sondern du solltest einfach vor der Installation checken, ob jenes Tool bekannt ist und wer dieses Tool finanziert (was du so oder so tun solltest auch bei einem klassischen Appstore).

Nun also zu der Entscheidung welchen Paketmanager du nutzen solltest.
Bei den meisten Linux Distros ist ein paket manager mit geliefert, falls du nicht weißt, welcher bei deinem Distro enthalten ist, solltest du Google mal fragen.
Bei Mac hingegen würde ich die Installation vom Paketmanager [homebrew](https://brew.sh/) stark empfehlen.
#### Wie installiere ich nun also Pakete mit meinem Paket Manager?
Ich werde im Folgenden nun den Ablauf zum Installieren der benötigten Programme für die Aufgaben beschreiben, wobei ich nur die Befehle für Ubuntu und Mac OS direkt erwähne, der Ablauf sollte jedoch für die anderen Linux paket manager ähnlich sein.

Nun also zu unserer ersten Installation: Python\
Python nutzen wir für die Abgabetests, um zu überprüfen, ob du eine Python version installiert hast schreibe folgendes in dein Terminal:
```
python3 -V
```
Falls dies nicht etwas wie: `Python 3.13.2` Ausgibt, müssen wir Python also erst mal installieren.
Wir wollen nämlich eigentlich den paket manager für Python mit installieren `pip`, da pip der de-facto Paketmanager für Python ist wird dieser meist automatisch mit installiert:
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

Nachdem wir den paket manager für python installiert haben, wollen wir auch gleich ein Paket mit diesem Installieren:
<div style="display: flex; gap: 20px;">
<div style="flex: 1;">
<strong>Für Ubuntu und mac</strong>
<pre><code class="language-bash">
pip install pytest
</code></pre>
</div>
<div style="flex: 1;">
<strong>Für Mac</strong>
<pre><code class="language-bash">
brew install pytest
</code></pre>
</div>
</div>

Nun benötigen wir noch einen C-Compiler damit du auch die Aufgaben erledigen kannst.
Was genau das ist und wie man sowas benutzt lernst du in den folgenden Aufgaben noch.

Wir nutzen als C-Compiler in diesem Beispiel gcc(GNU Compiler Collection), aber du kannst den C-Compiler deiner Wahl nutzen:
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
Nein? Dann kannst du ja mal aus Spass, dich durch die verlinkte [Installation vom C-Compiler](https://gcc.gnu.org/install) durchklicken.

Nun zum letzten Tool welches du benötigst: Git\
Git ist ein Versionierungungstool, wobei wir auf was das genau heißt in Aufgabe00 nochmal genauer eingehen werden.
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

---
</details>


# Start !
Na ja, fast haha. Wir müssen uns noch unser Projekt aus dem Internet auf die Festplatte holen.\
Dafür öffne erst einmal das Terminal und führe den Befehl `ls` aus.
Dieser Befehl bedeutet list und er listet, wie der Name schon vermuten lässt, alle Ordner und Dateien in deinem aktuellen Ordner auf.
Jedes Unix basierte Dateisystem (also so gut wie alles ausser Windows) ist wie eine Wurzelstruktur aufgebaut, beginnend mit der sogenannten Root `/`.\
Als Nächstes solltest du versuchen in einen Ordner zu navigieren, in welchen du das Repository reinkopieren willst, hilfreiche Befehle dafür sind:
```bash
# list
ls
# change directory: also gehe in Ordner
cd Ordnername
# cd zu home Ordner (meist ein guter Anfang für seine eigene Ordnerstruktur)
cd ~
# gehe in den nächst höheren (Parent) Ordner
cd ..
# make directory: erstelle einen Ordner
mkdir Ordnername
```
Siehe auch: [cheatsheet](https://images.velog.io/images/hy9202/post/8f1f2c7e-4edf-49ec-9c9e-380ade1325a8/command-line-cheat-sheet-large01.png)

### Ein Repository Forken:
<details>
<summary>Falls dies dein erster Kontakt mit git ist, Klicke mich an</summary>

Für dieses Projekt ist es am einfachsten sich ein Profil bei [Github](https://github.com/) zu erstellen, falls du dies noch nicht getan hast.
Nun solltest du bei git im Terminal, einstellen welche E-Mail und Name bei den Commits angegeben werden soll:
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

Als kleiner Tipp: richte dir SSH ein, sonst musst du jedes Mal dein Passwort angeben, wenn du etwas pushen willst.
Dafür solltest du erst einmal ein Tool welches ssh keys generieren kann wie **openSSH installieren** mit deinem Paketmanager.

<div style="display: flex; gap: 20px;">
<div style="flex: 1;">
<strong>Für Ubuntu</strong>
<pre><code class="language-bash">
sudo apt-get install openssh-client
</code></pre>
</div>
<div style="flex: 1;">
<strong>Für Mac</strong>
<pre><code class="language-bash">
brew install openssh
</code></pre>
</div>
</div>

Nun kannst du einen **ssh-key** in deinem Terminal **generieren**:
```bash
# ersetze your_email@example.com durch deine GitHub-E-Mail-Adresse
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Nun musst du noch den **SSH-Schlüssel zum SSH-Agenten hinzufügen**.
Dafür starten wir erst einmal den SSH-Agenten im Hintergrund: `eval "$(ssh-agent -s)"`\
und fügen halt den Schlüssel mit folgenden Befehlen hinzu:
<div style="display: flex; gap: 20px;">
<div style="flex: 1;">
<strong>Für Ubuntu</strong>
<pre><code class="language-bash">
ssh-add ~/.ssh/id_ed25519
</code></pre>
</div>
<div style="flex: 1;">
<strong>Für Mac</strong>
<pre><code class="language-bash">
open ~/.ssh/config
# wenn die Datei nicht existiert:
touch ~/.ssh/config
# Öffne deine ~/.ssh/config-Datei
# Kopiere das Folgende rein
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
# als letztes führe aus:
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
</code></pre>

**Hinweis**

Wenn du keine Passphrase zu deinem Schlüssel hinzufügen möchtest, solltest du die `UseKeychain-Zeile` auslassen.\
Wenn ein Bad configuration option: usekeychain-Fehler angezeigt wird, füge dem Abschnitt `Host *.github.com` der Konfiguration eine zusätzliche Zeile hinzu.
```
Host github.com
  IgnoreUnknown UseKeychain
```
</div>
</div>

Nach diesen Schritten sind wir bereit den **Key zu unserem GitHub profil hinzuzufügen**.
Wir nutzen `cat` um unseren Key ins Terminal zu Printen:
```bash
cat ~/.ssh/id_ed25519.pub
# das sollte folgendes Auswerfen:
ssh-ed25519  ___DEIN_KEY___  Kommentar
```

Auf GitHub klicken Sie auf Ihr Profilbild in der oberen rechten Ecke > Klicken Sie im Dropdown-Menü auf „Einstellungen“.
Klicken Sie in der Seitenleiste mit den Benutzereinstellungen auf der linken Seite auf „SSH- und GPG-Schlüssel“.
Klicken Sie auf die grüne Schaltfläche „Neuer SSH-Schlüssel“ und geben Sie im Feld „Titel“ einen aussagekräftigen Namen für Ihren Schlüssel ein (z. B. „persönliches MacBook“).
Wähle bei dem Dropdown-Menü Authentifizierung aus.\
Fügen Sie den kopierten Inhalt (also `___DEIN_KEY___` ) vom öffentlichen SSH-Schlüssels in das Feld „Schlüssel“ ein und klicke den ‘Add SSH key’ button.
Bei dem ersten nutzen wirst du gefragt: `Are you sure you want to continue connecting`.
Stellen Sie sicher, dass der Fingerabdruck des Schlüssels mit dem RSA-Fingerabdruck des öffentlichen Schlüssels von Github übereinstimmt, und geben Sie dann „yes“ ein.
Damit ist alles fertig eingerichtet.\
[Quelle](https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac)

---

</details>

Forken bedeutet, dass du eine **eigene Kopie eines Projektes** auf GitHub (oder GitLab etc.) erstellst.
Du kannst dann in deiner eigenen Version experimentieren, Dinge verändern oder verbessern – ohne das Original zu verändern.

Stell dir vor, jemand hat ein cooles Projekt gebaut, und du möchtest darauf aufbauen oder es verbessern.
Mit einem Fork bekommst du deine eigene Version, mit der du machen kannst, was du willst.
Wenn du später möchtest, dass deine Änderungen ins Original übernommen werden, kannst du dem ursprünglichen Autor einen Pull Request schicken.

Damit du deine Lösungen implementieren kannst, musst du dir deine ganz eigene Version vom Repository holen.

**Forke dieses Repository** über den "Fork"-Button oben rechts, dies ist nun dein eigenes Repository auf welchem du arbeiten wirst. 

### Ein Repository klonen:
Klone nun dein **eigenes** Projekt (also deinen Fork).
Beim Aufruf des Befehls wirst du gegebenenfalls nach deinem Nutzeraccount gefragt.
Um den Accountnamen und das Password nicht immer eingeben zu müssen, kann der Zugang per [SSH eingerichtet](#ein-repository-forken)) werden.
```
git clone <Adresse vom grünen code button oben rechts>
```

Nach dem Klonen findest du das Repository in dem dabei neu erstellten Ordner, checke dies mit `ls`.
Dort kannst du jetzt deine Abgabendateien versionieren und Branches verwalten.
### Nach dem Clonen:
Da du für den nächsten Schritt eine Datei ausführen musst, empfehle ich dir kurz in das [test file](test.bash) zu schauen um zu überprüfen, was es macht.
(Am besten einfach die Kommentare lesen und Befehle die suspekt aussehen googeln)

Da du nun also überprüft hast, dass die Datei kein Virus ist oder mir vertraust, kannst du nun das Projektsetup vollenden, dafür musst du mein **test bash file ausführen**. Dabei macht der erste Befehl es zu einem executable und der zweite führt es aus:
```bash
# ausführbar machen
chmod +x test.bash
# ausführen
./test.bash
```
Stelle dabei sicher, dass du im Projektordner bist und wenn du `ls` aufrufst die Datei `test.bash` angezeigt wird.

Wie du schon bemerkt hast, führt `test.bash` die Tests für dich automatisch und intelligent aus.
Falls du also deine Abgabe testen willst, kannst du dies durch den Befehl`./test.bash` ganz einfach machen.
Um alle Tests auszuführen einmal, kannst du auch einfach `pytest` ausführen.

Falls dies alles geklappt hat und keine Fehler ausgespuckt wurden, bist du ready dich an `Aufgabe00` zu versuchen.
Schaue dafür einfach in den Ordner [Aufgabe00](Aufgabe00/README.md).

---
# DA WORK IN PROGRESS

Falls auf dem main repository, also diesem, etwas verändert wird, was du dir auf deine Version vom Repository holen willst, ist hier eine Anleitung dafür:

In einer Standardkonfiguration gibt es in der Regel einen origin (dein Fork) und einen Upstream-Remote – letzterer ist meist das Ursprungs Repository, zu dem du beitragen möchtest.\
In unserem Fall willst du zwar nichts beitragen, aber updates vom Ursprungs Repository erhalten, dafür musst du einmalig den Upstream festlegen:
```
git remote add upstream https://github.com/JoJo149/DieBasicsDerInformatik.git
```
Um nun Veränderungen vom upstream zu pullen/fetchen und danach in dein lokalen Branch zu mergen/rebase (einfach gesagt schlau einfügen), führe die folgenden Befehle aus:
```
git fetch upstream
git checkout main
git rebase upstream/main
git push origin main
```
