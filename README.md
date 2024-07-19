Eintrichtung und Aktivierung der virtuellen Umgebung, sowie installation benötigter Pakete:

##Erklärung##
Eine virtuelle Umgebung (venv) dient dazu, eine isolierte Python-Umgebung für ein Projekt zu erstellen. Dadurch können spezifische Versionen von Python-Paketen installiert werden, ohne das globale Python-Setup zu beeinflussen. Dies vermeidet Konflikte zwischen verschiedenen Projekten und stellt sicher, dass das Projekt auf verschiedenen Systemen konsistent läuft.

##Commands in das Terminal einfügen##
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\activate
pip install -r requirements.txt

##Wichtige Info##
Die Befehle
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
und
.\.venv\Scripts\activate
müssen nach jedem Neustart der IDE ins Terminal eingefügt werden, damit die benötigten Pakete korrekt verwendet werden. Der erste Befehl (python -m venv .venv) muss nur ein einziges Mal ausgeführt werden, da dieser die virtuelle Umgebung erstellt, und die anderen beiden diese aktivieren.

##Randnotiz##
Der Befehl "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass" wird benötigt, um die PowerShell-Ausführungsrichtlinie temporär zu ändern, damit du Skripte ausführen kannst, die in deinem virtuellen Environment enthalten sind. Dies ist notwendig, weil PowerShell standardmäßig Sicherheitsrichtlinien hat, die das Ausführen von Skripten verhindern können.