from flask import Blueprint, render_template, request, session
from flask_login import current_user
from main import Comment


chemPs = Blueprint("chemPs", __name__)

@chemPs.route('/chemistry')
def index():
    return render_template('chemistryBase.html')


@chemPs.route('/chemistry/ph')
def pH():
    return render_template("chemistryPages/ph.html", comments=Comment.query.filter(Comment.page == request.url), current_user=current_user)


@chemPs.route("/chemistry/electronegativity")
def electronegativity():
    return render_template("chemistryPages/electronegativity.html", comments=Comment.query.filter(Comment.page == request.url), current_user=current_user)


@chemPs.route("/chemistry/periodicTable", methods=['GET'])
def periodicTable():
    return render_template("chemistryPages/periodicTable.html", comments=Comment.query.filter(Comment.page == request.url), current_user=current_user)
