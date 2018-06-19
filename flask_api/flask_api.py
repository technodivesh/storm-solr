#!flask/bin/python
from flask import Flask, jsonify
# from flask_mysqldb import MySQL
from faker import Faker

fake = Faker()
app = Flask(__name__)
# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'storm'
# app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

# mysql.init_app(app)


# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]

# @app.route('/api/v1/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})


# @app.route('/api/v1/products',methods=['GET'])
# def get():
#     cur = mysql.connect().cursor()
#     cur.execute('''select * from storm.products''')
#     r = [dict((cur.description[i][0], value)
#               for i, value in enumerate(row)) for row in cur.fetchall()]
#     return jsonify({'myCollection' : r})

@app.route('/',methods=['GET'])
def default():
    api_text = "try --  /api/v1/profiles"
    return api_text

@app.route('/api/v1/profiles',methods=['GET'])
def fake_profile():
    return jsonify([fake.simple_profile() for _ in range(10)])


if __name__ == '__main__':
    app.run(debug=True)