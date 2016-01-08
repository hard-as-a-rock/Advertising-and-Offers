from flask import render_template, url_for, flash, request, redirect, jsonify


from app import app, db
from models import User, UserAdvertisement, Advertisement
from forms import UserForm



@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
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