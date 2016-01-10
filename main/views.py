from flask import g, render_template, url_for, flash, request, redirect, jsonify, session
from flask.ext.login import (LoginManager, login_user, logout_user,
                             login_required, current_user)

from app import app, db, login_manager
from models import User, UserAdvertisement, Advertisement
from forms import UserForm, LoginForm


@login_manager.user_loader
def get_user(ident):
    return User.query.get(ident)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({
                'status': 'ok',
            })
        else:
            return jsonify({
                'status': 'error',
                'input_errors': form.errors
            })

    ctx = {
        'form': form
    }

    return render_template('registration.html', **ctx)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            remember_me = False
            if 'remember_me' in request.form:
                remember_me = True
            login_user(form.user, remember=remember_me)
            return jsonify({
                'status': 'ok'
            })
        else:
            return jsonify({
                'status': 'error',
                'errors': form.errors
            })
    ctx = {
        'form': form
    }
    return render_template('login.html', **ctx)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))