from library import db
from library.models.all_models import User
from flask import redirect, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from . import auth


class RegisterForm(FlaskForm):
    login = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField("Register")


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.login.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            flash("Passwords don't match", "error")
            return render_template("register.html", title="Register", form=form)

        user = User.query.filter_by(login=username).first()
        if user:
            flash("User already exists", "error")
            return render_template("register.html", title="Register", form=form)

        user = User(login=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash("User created", "success")
        return render_template("register.html", title="Register", form=form)
    return render_template("register.html", title="Register", form=form)
