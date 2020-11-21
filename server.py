import os
from flask import Flask, redirect, request, render_template
import sqlite3

#DATABASE = '.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)






























if __name__ == "__main__":
	app.run(debug=True)
