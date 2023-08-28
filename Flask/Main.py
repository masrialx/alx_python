from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class list(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    email = db.Column(db.String(length=120), nullable=False)  # Corrected this line


List = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "id": 1
    },
    {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "id": 2
    },
    {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "id": 3
    },
    {
        "name": "Bob Williams",
        "email": "bob@example.com",
        "id": 4
    },
    {
        "name": "Eve Brown",
        "email": "eve@example.com",
        "id": 5
    },
    {
        "name": "Michael Lee",
        "email": "michael@example.com",
        "id": 6
    },
    {
        "name": "Sarah Miller",
        "email": "sarah@example.com",
        "id": 7
    },
    {
        "name": "David Johnson",
        "email": "david@example.com",
        "id": 8
    },
    {
        "name": "Emily Davis",
        "email": "emily@example.com",
        "id": 9
    },
    {
        "name": "Daniel Wilson",
        "email": "daniel@example.com",
        "id": 10
    }
]

@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html',List=List)

@app.route('/about')
def About():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)
