import os
import bcrypt
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'database.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/Home")
def admin():
    username = request.cookies.get('username')
    usertype = "null"
    if 'usertype' in session:
        usertype = escape(session['usertype'])
    if usertype == "Admin":
        return render_template('home.html', msg = 'logged in as admin', username = username)
    else:
        return render_template('selectPDF.html', msg = 'no access', username = username)

app.secret_key = 'bqxe6dx12x7fxa9xd5xdcycxx04xdf4xb6chxca@;Pxdax02xcf' #using os.urandom(24)

@app.route("/Login", methods = ['GET','POST'])
def login():
    if request.method=='POST':
        uName = request.form.get('username', default="Error")
        pw = bcrypt.hashpw(request.form.get('password', default="Error").encode(),b'$2b$12$5nU0TVBvc2ZD2mLE6PztrO')
        if checkCredentials(uName, pw):
            print("checking login details")
            session['username'] = request.form['username']
            if (uName =="Admin"):
                session['usertype'] = 'Admin'
                resp = make_response(render_template('home.html', msg='hello '+uName, username = uName))
            else:
                session['usertype'] = 'Staff'
                resp = make_response(render_template('selectPDF.html', msg='hello '+uName, username = uName))
        else:
            resp = make_response(render_template('login.html', msg='Incorrect login'))
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('Login.html', msg='', username = username)

def checkCredentials(uName, pw):
    return pw == b"$2b$12$5nU0TVBvc2ZD2mLE6PztrOcdB.SwZnfS5Ff7PK3rQYK.gjJtu967K"

@app.route("/Index")
def index():
    return render_template('index.html')

@app.route("/Users")
def users():
    username = request.cookies.get('username')
    usertype = "null"
    if 'usertype' in session:
        usertype = escape(session['usertype'])
    if usertype == "Admin":
        return render_template('users.html', username = username)
    else:
        return render_template('selectPDF.html', msg = 'no access to users page', username = username)

@app.route("/FetchUser")
def fetchuserinfo():
    db = sqlite3.connect("database.db")
    curs = db.cursor()
    curs.execute("SELECT username, role FROM Users")
    results = curs.fetchall()
    username_array = []
    role_array = []
    for idx, val in enumerate(results):
        username_array.append(results[idx][0])
        role_array.append(results[idx][1])
    print(username_array,role_array)
    curs.close()
    db.close()
    return render_template("users.html", username = username_array, role = role_array)

@app.route("/Customers")
def customer():
    if request.method == 'GET':
        username = request.cookies.get('username')
        usertype = "null"
        if 'usertype' in session:
            usertype = escape(session['usertype'])
        if usertype == "Admin":
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("SELECT customerName, address, deliveryAddress FROM Customers") #check that this is secure as it doesn't use the "?"
                data = cur.fetchall()
                print(data)
            except:
                print('there was an error', data)
                conn.close()
            finally:
                conn.close()
                # return str(data)
                return render_template('customers.html', data = data)
        else:
            return render_template('selectPDF.html', msg = 'no access to users page', username = username)


if __name__ == "__main__":
	app.run(debug=True)
