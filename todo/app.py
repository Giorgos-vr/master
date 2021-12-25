from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240))
    complete = db.Column(db.Boolean)



@app.route('/')
def index():
    todo_list = todo.query.all()
    return render_template('base.html', todo_list=todo_list)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)