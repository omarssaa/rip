from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime
import hashlib


interactive = Blueprint("interactive", __name__)


from main import User, db, Comment


@interactive.route('/login', methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        email = request.form["email"]
        psd = request.form["psd"]
        if request.form.get('remember'):
            remember = True
        else:
            remember = False

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Email not correct")
            return redirect(url_for('interactive.login'))

        if user.password != hashlib.sha256(psd.encode()).hexdigest():
            flash("Password is not correct")
            return redirect(url_for('interactive.login'))


        login_user(user, remember=remember)
        session['user_id'] = user.get_id()

        return redirect('/profile')
    return render_template("login.htm")


@interactive.route('/signup', methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        psd = request.form["psd"]

        userCheck = User.query.filter_by(email=email).first()
        userCheckByName = User.query.filter_by(name=name).first()

        if userCheck:
            flash("Email already in use.")
            return redirect('/signup')
        elif userCheckByName:
            flash("User name already in use.")
            return redirect('/signup')

        newUser = User(email=email, name=name, password=hashlib.sha256(psd.encode()).hexdigest())

        db.session.add(newUser)
        db.session.commit()

        return redirect("/login")
    return render_template('signup.htm')

@interactive.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(request.referrer)


@interactive.route('/comment/post', methods=['GET','POST'])
@login_required
def post_comment():
    if request.method == 'POST':
        comment = request.form['comment']
        dt= datetime.now()
        new_comment = Comment(comment_text=comment, commenter_id=session['user_id'], comment_date=dt, page=request.referrer)
        db.session.add(new_comment)
        db.session.commit()

    return redirect(request.referrer)
