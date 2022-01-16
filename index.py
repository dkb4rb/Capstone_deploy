#!/usr/bin/python3
"""
    Import libraries
"""
import sqlite3
from flask import Flask , render_template

app = Flask("Root")

@app.route('/')
def home():
    # returning string
    return render_template("index.html")

pages = ["/html/states.html", "/html/search.html"]
@app.route(pages[0])
def bar():
    # returning search bar
    return render_template(pages[0])

@app.route(pages[1])
def states():
    # returning states gallery
    return render_template(pages[1])

def err_pa():
    def get_db_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn
    
    
    if __name__ == "__main__":        
        if get_db_connection() is False:
            render_template()


if __name__ == "__main__":
    app.run(debug=True, port=2427)
    
    con = err_pa()
    print(con)
