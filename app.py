# Flask Basic CRUD Application
# C - Create
# R - Read
# U - Update
# D - Delete

# Import the required libraries
from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

# Configure Flask app
app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'books'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)


# Read from Database
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM book_info")
    data = cur.fetchall()

    return render_template('index.html', data=data)


# Insert new entry in Database
@app.route('/insert/', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pub_date = request.form['pub_date']
        pages = request.form['pages']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO book_info(title, author_name, publication_date, pages, price) VALUES(%s,%s,%s,%s,%s)",
                    [title, author, pub_date, pages, price])
        mysql.connection.commit()
        cur.close()

    return redirect(url_for('index'))


# Update entry in Database
@app.route('/update/<string:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pub_date = request.form['pub_date']
        pages = request.form['pages']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE book_info SET title=%s, author_name=%s, publication_date=%s, pages=%s, price=%s WHERE id=%s",
                    [title, author, pub_date, pages, price, id])
        mysql.connection.commit()
        cur.close()

    return redirect(url_for('index'))


# Delete entry from Database
@app.route('/delete/<string:id>/', methods=['GET', 'POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM book_info WHERE id=%s", [id])
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
