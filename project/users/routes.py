from flask import flash, render_template, abort
from . import users_blueprint

@users_blueprint.route('/admin')
def admin():
    abort(403)

@users_blueprint.route("/about")
def about():
    flash('Thanks for learning about this site!', 'info')
    return render_template("users/about.html", name="Puneeth Y S")