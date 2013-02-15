from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('hello.cfg')
db = SQLAlchemy(app)

class Greeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True)
    
    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return '<Greeting %r>' % self.username
    
db.create_all()
db.session.add(Greeting('Hello'))
db.session.add(Greeting('Ahoy'))
db.session.add(Greeting('G\'day'))
db.session.add(Greeting('Hey'))
db.session.add(Greeting('Howdy'))
db.session.commit()

@app.route("/")
def hello():
    greets = Greeting.query.all()
    return greets

if __name__ == "__main__":
    app.run()
