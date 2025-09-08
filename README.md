# Einführung in die Informatik

**Aufgaben sind im jeweiligen Branch und dort im Ordner.**

Dieses Tutorial/Einführung ist nur für Linux oder OSX (also Mac OS) user geschrieben und wird vielleicht, wenn ich die Zeit dazu finde für windows erweitert.

### Dependencies

- [python](https://www.python.org/downloads/)
  - [pytest](https://pypi.org/project/pytest/)
- [C compiler](https://gcc.gnu.org/install/)
- [git](https://git-scm.com/downloads)

### Fetch Updates

Falls auf dem main repository, also dem ursprünglichen [Repository](https://github.com/JoJo149/DieBasicsDerInformatik), etwas verändert wird, was du dir auf deine Version vom Repository holen willst, ist hier eine Anleitung dafür:

Lege **einmalig** den Upstream festlegen:
```
git remote add upstream https://github.com/JoJo149/DieBasicsDerInformatik.git
```
Um nun Veränderungen vom upstream zu pullen/fetchen und danach in dein lokalen Branch zu mergen/rebase, führe die folgenden Befehle aus:
```bash
git fetch upstream
git checkout main
git rebase upstream/main
# falls sich das setup.bash verändert hat, führe hier setup aus
git push origin main
```

### setup:

Nur falls das setup.bash sich verändert hat, führe es aus:
```
chmod +x setup.bash
./setup.bash
```
Stelle dabei sicher, dass du im Projektordner bist und wenn du `ls` aufrufst die Datei `setup.bash` angezeigt wird.
