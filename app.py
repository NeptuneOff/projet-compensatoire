from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User
from forms import LoginForm, RegisterForm
import requests
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Accueil / Auth ---
@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return redirect(url_for('players'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('players'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Inscription réussie. Vous pouvez maintenant vous connecter.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('players'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('players'))
        flash('Nom d’utilisateur ou mot de passe invalide.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- Appels API ---
API_BASE = 'https://api.balldontlie.io/v1'

from config import BALLEDONTLIE_API_KEY
HEADERS = {"Authorization": f"Bearer {BALLEDONTLIE_API_KEY}"}

def safe_get(url, params=None):
    try:
        resp = requests.get(url, params=params, headers=HEADERS, timeout=8)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Erreur API {url}: {e}")
        return None


@app.route('/players')
@login_required
def players():
    data = safe_get(f'{API_BASE}/players', params={'per_page': 100})
    players = data.get('data', []) if data else []
    if not players:
        flash("Impossible de récupérer les joueurs depuis l’API externe.")
    return render_template('players.html', players=players)

@app.route('/players/<int:player_id>')
@login_required
def player_detail(player_id):
    player_resp = safe_get(f'{API_BASE}/players/{player_id}')
    if not player_resp or "data" not in player_resp:
        flash("Joueur introuvable.")
        return redirect(url_for('players'))
    player = player_resp["data"]   # 👈 extraire les données réelles
    return render_template('player_detail.html', player=player)


@app.route('/teams')
@login_required
def teams():
    data = safe_get(f'{API_BASE}/teams')
    teams = data.get('data', []) if data else []
    if not teams:
        flash("Impossible de récupérer les équipes depuis l’API externe.")
    return render_template('teams.html', teams=teams)

@app.route('/teams/<int:team_id>')
@login_required
def team_detail(team_id):
    team_resp = safe_get(f'{API_BASE}/teams/{team_id}')
    if not team_resp or "data" not in team_resp:
        flash("Équipe introuvable.")
        return redirect(url_for('teams'))
    team = team_resp["data"]   # 👈 extraire les données réelles

    players_data = safe_get(f'{API_BASE}/players', params={'team_ids[]': team_id, 'per_page': 100})
    players = players_data.get('data', []) if players_data else []
    return render_template('team_detail.html', team=team, players=players)


@app.route('/games')
@login_required
def games():
    games = []
    page = 1
    while True:
        data = safe_get(f'{API_BASE}/games', params={'per_page': 100, 'page': page})
        if not data or not data.get('data'):
            break
        games.extend(data['data'])
        page += 1
    for g in games:
        try:
            iso = g['date'].rstrip('Z')
            g['local_date'] = datetime.fromisoformat(iso).strftime('%d/%m/%Y')
        except Exception:
            g['local_date'] = g.get('date', '')
    if not games:
        flash("Impossible de récupérer les matchs depuis l’API externe.")
    return render_template('games.html', games=games)

@app.route('/games/<int:game_id>')
@login_required
def game_detail(game_id):
    game_resp = safe_get(f'{API_BASE}/games/{game_id}')
    if not game_resp or "data" not in game_resp:
        flash("Match introuvable.")
        return redirect(url_for('games'))
    game = game_resp["data"]   # 👈 extraire les vraies données

    try:
        iso = game['date'].rstrip('Z')
        game['local_date'] = datetime.fromisoformat(iso).strftime('%d/%m/%Y')
    except Exception:
        game['local_date'] = game.get('date', '')
    return render_template('game_detail.html', game=game)


if __name__ == '__main__':
    app.run(debug=True)
