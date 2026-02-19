from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '1234567890')


# Utilisateur de démonstration (en production, utiliser une base de données)
UTILISATEUR_DEMO = {
    'username': 'etudiant',
    'password': 'edt2026'
}


@app.route('/')
def login_requierd(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vérification simple (à remplacer par une vraie vérification)
        if username == UTILISATEUR_DEMO['username'] and password == UTILISATEUR_DEMO['password']:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            message = "Identifiants incorrects. Essayez à nouveau."
    return render_template('login.html', message=message)


@app.route('/home')
@login_requierd
def home():
    return render_template('home.html', username=session['username'])

@app.route('/À propos')
@login_requierd
def about():
    return render_template('about.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
