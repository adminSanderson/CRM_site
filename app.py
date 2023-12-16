# from flask import Flask, render_template, url_for
# from sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CRM.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.id


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Manager %r>' % self.id


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameP = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Project %r>' % self.id


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameT = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


class SubTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameST = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    comm = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<SubTask %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/entry')
def signup():
    return render_template("entry.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/task_table')
def task():
    return render_template("task_table.html")

if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=True)
