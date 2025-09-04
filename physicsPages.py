from flask import Blueprint, render_template, request
from flask_login import current_user

from main import Comment


phyPs = Blueprint("phyPs", __name__)

@phyPs.route('/physics/velocity')
def velocity():
    return render_template("physicsPages/velocity.htm", comments=Comment.query.filter(Comment.page == request.url), current_user=current_user)


@phyPs.route('/physics/kinematics')
def kinematics():
    return render_template("physicsPages/kinematics.html", comments=Comment.query.filter(Comment.page == request.url), current_user=current_user)

@phyPs.route('/physics/weight')
def weight():
    return render_template("physicsPages/weight.html", comments=Comment.query.filter(Comment.page == request.url), current_user=current_user)