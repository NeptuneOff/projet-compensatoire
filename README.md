# 🏀 Ynov Basket – Projet Compensatoire B2

## 📌 Description

Ce projet est une application web développée avec **Flask (Python)** qui permet de :

- Gérer l’**authentification** (inscription et connexion avec mots de passe hashés).
- Consulter les **joueurs NBA**, les **équipes** et les **matchs** via l’API publique [balldontlie.io](https://www.balldontlie.io/).
- Accéder aux **détails** de chaque joueur, équipe et match.

L’objectif est de démontrer l’utilisation d’un framework web Python, l’intégration d’une API externe et la mise en place d’une base SQLite pour la gestion des utilisateurs.

---

## 📂 Structure du projet

```
projet-compensatoire/
├── app.py
├── config.py
├── forms.py
├── models.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── players.html
│   ├── player_detail.html
│   ├── teams.html
│   ├── team_detail.html
│   ├── games.html
│   └── game_detail.html
└── static/
```

---

## ⚙️ Installation

### 1. Installer Python
Téléchargez la dernière version de **Python 3.10+** depuis : [python.org](https://www.python.org/downloads/).  
👉 Cochez bien **Add Python to PATH** à l’installation.

### 2. Cloner le projet (si sur GitHub)
```bash
git clone https://github.com/votre-utilisateur/projet-compensatoire.git
cd projet-compensatoire
```

Ou placez simplement les fichiers dans un dossier `projet-compensatoire`.

### 3. Créer un environnement virtuel
Sous **PowerShell** :
```powershell
py -m venv venv
.env\Scripts\Activate.ps1
```

### 4. Installer les dépendances
```powershell
pip install -r requirements.txt
```

---

## 🔑 Configuration API

L’API **balldontlie v1** requiert une clé API gratuite.

1. Inscrivez-vous sur 👉 [balldontlie.io](https://balldontlie.io).  
2. Récupérez votre **clé API** dans votre tableau de bord.  
3. Ouvrez `config.py` et ajoutez :
   ```python
   BALLEDONTLIE_API_KEY = "votre_cle_api"
   ```

---

## 🚀 Lancement du projet

Toujours dans votre terminal PowerShell, dans le dossier du projet :

```powershell
.env\Scripts\Activate.ps1
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```

Le serveur démarre sur 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Fonctionnalités

- 🔑 **Authentification**
  - Inscription
  - Connexion
  - Déconnexion

- 🏀 **NBA Data**
  - Liste des joueurs + détails (taille, poids, position, équipe…)
  - Liste des équipes + détails (ville, conférence, division…)
  - Liste des matchs + détails (date, équipes, scores)

---

## 📸 Exemple d’utilisation

1. Allez sur [http://127.0.0.1:5000/register](http://127.0.0.1:5000/register) pour créer un compte.
2. Connectez-vous via [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login).
3. Naviguez vers :
   - `/players` → liste des joueurs
   - `/teams` → liste des équipes
   - `/games` → liste des matchs

---

## 👨‍💻 Technologies utilisées

- **Python 3.10+**
- **Flask**
- **Flask-Login**
- **Flask-WTF**
- **SQLite (SQLAlchemy)**
- **Bootstrap 5** (interface)

---

## ✨ Auteur

Projet développé dans le cadre du **Devoir Compensatoire B2 – Ynov**.  
Réalisé par : **Karl Daval-Leclercq**
