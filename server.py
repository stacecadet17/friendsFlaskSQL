from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    query = "SELECT first_name, age, created_at FROM friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', all_friends = friends)

@app.route('/newfriend', methods=['POST'])
def newfriend():
    query = "INSERT INTO friends(first_name, age, created_at) VALUES(:name, :age, NOW());"
    data = {
        "name": request.form['name'],
        "age": request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
