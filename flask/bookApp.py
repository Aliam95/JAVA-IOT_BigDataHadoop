#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
import json
import pandas as pd
app = Flask(__name__)

dfBooks = pd.read_json("../flask/books.json")

@app.route('/')
def index():
    return "Hello world!"

@app.route('/books')
def books():
    return dfBooks.to_json(orient ='records')

@app.route('/books/<book>')
def load (book):
    if book is None:
        return ('please enter a valid isbn')
    else:
	return dfBooks[dfBooks.isbn == book].to_json(orient ='records')

if __name__ == '__main__':
    app.run(debug=True) 
