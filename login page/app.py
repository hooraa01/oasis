from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms import EmailField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

users = {}

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Length(min=6, max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        if username in users:
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))

        users[username] = {'email': email, 'password': password}
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in users and users[username]['password'] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('secured'))

        flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

@app.route('/secured')
def secured():
    if 'username' in session:
        return render_template('secured.html', username=session['username'])
    flash('You need to login first', 'danger')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
