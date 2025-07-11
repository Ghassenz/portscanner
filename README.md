# 🔍 Port Scanner GUI

**Port Scanner GUI** est une application Linux en Python (Tkinter) permettant de scanner les ports TCP ouverts d'une adresse IP cible dans une plage définie.

---

## 🖥️ Fonctionnalités

- ✅ Interface graphique avec Tkinter
- ✅ Scan d'une IP cible dans une plage de ports (ex : 20–1024)
- ✅ Détection uniquement des ports ouverts
- ✅ Affichage lisible avec barre de statut
- ✅ Version `.deb` installable avec icône et raccourci menu

---

## 📷 Capture d’écran

*(Ajouter ici `scan.png` si disponible)*  
![Scan](scan.png)

---

## 📦 Installation

```bash
wget https://github.com/Ghassenz/portscanner/releases/download/v1.0/scanner-gui.deb
sudo dpkg -i scanner-gui.deb
```

---

## 🚀 Lancement

- Depuis le **menu Linux** : `Port Scanner`
- Ou via le terminal :
```bash
portscanner
```

---

## 🔧 Dépendances

```bash
sudo apt install python3 python3-tk
```

---

## 📁 Structure du paquet

```
scanner-deb/
├── DEBIAN/control
├── usr/
│   ├── bin/portscanner
│   └── share/
│       ├── applications/portscanner.desktop
│       └── icons/hicolor/128x128/apps/portscanner.png
```

---

## 👤 Auteur

Développé par **Ghassenz**  
Projet personnel pour l’apprentissage du développement et de la cybersécurité sous Linux.

🔗 [https://github.com/Ghassenz](https://github.com/Ghassenz)

---

## ✅ Licence

Projet open-source — libre d’utilisation pour apprentissage et tests en environnement local.
