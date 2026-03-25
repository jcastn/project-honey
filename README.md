# project-honey

Lors d’un cours de cybersécurité dans le cadre de mes études, j’ai eu l’occasion de travailler sur un projet autour de la sécurité informatique, mêlant développement, réseaux et analyse de vulnérabilités.

L’objectif était d'étudier comment une macro exécutée à l’ouverture d’un document Word pourrait servir de vecteur d’installation d’un keylogger (enregistreur de frappes), puis analyser les mécanismes de collecte et d’exfiltration de données. Le tout dans un cadre strictement pédagogique, afin de comprendre ces techniques pour mieux s’en protéger.

**⚠️ Avertissement Légal : Le code est fourni à des fins strictement éducatives et d'audit de sécurité. L'usage de ces outils sur un système tiers sans consentement explicite est illégal et passible de sanctions pénales.**

Le projet contenait 3 grandes parties : 
- Le développement du cheval de Troie (en Python dans mon cas) 
- La création de la macro (en Visual Basic)
- L’exfiltration des données (via un Bot Discord)

---
## Explication du script Python   

Le script Python qui compose le Project Honey, fonctionne comme suit : 

Il commence par l'importation plusieurs modules : 
- `Pynput` → Enregistrer les touches
- `Datetime` et `Time`→ Obtenir l’heure et gérer le temps
- `OS` et `Platform` → Obtenir des infos sur l’OS et le materiel de l’utilisateur
- `Discord` → Envoyer les données sur Discord

Ensuite il prépare un message d’introduction (avec date et heure, nom du PC, OS…), et il enregistre pendant 15min toutes les touches pressées par l’utilisateur.

Chaque minute, il envoie un compte rendu de l’enregistrement sur discord avec le bot `Project Honey` et il enregistre aussi le tout dans un fichier `projecthoney.txt` se trouvant dans le dossier Documents de l’utilisateur (cela pourrait être n’importe où sur le PC, mais il a été mis là pour plus de simplicité).

Enfin, l’executable `project-honey.exe` peut être créé à partir du script en python avec le module PyInstaller.
- `pyinstaller --onefile --noconsole "C:\Users\[...]\ProjectHoney\main.py"`

Quand le script Python est lancé depuis VSCode, il fonctionne sans désactiver l’antivirus, par contre quand il est sous forme d'exécutable (`.exe`), il ne fonctionne que lorsque l’anti-virus de l’ordinateur est désactivé.

---

Une fois lancé, le logiciel apparait dans le gestionnaire des tâches.
Les résultats s'affichent sur Discord ainsi que dans le fichier `projecthoney.txt`, sous cette forme : 

```
------------------------------------------------------------------------
Session du xx/xx/xxxx - xx:xx:xx
User: xxxxx - OS: xxxxxxx xx.x.xxxxx - Hostname: PC-xxxxxx
bonjour [Key-space]
je [Key-space]
tape [Key-space]
du [Key-space]
texte [Key-enter]
------------------------------------------------------------------------
```
