from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from keys.api import string_conn

app = Flask(__name__)
app.config['MONGO_URI']= string_conn

mongo = PyMongo(app)

@app.route('/users',methods=['POST'])
def create_user():
    
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and password and email:
        #cifrar password
        hashed_password=generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username':username,'email':email,'password':hashed_password}
        )
        response = {
            'id': str(id),
            'username':username,
            'password':hashed_password,
            'email':email
        }
        return response
    else:
        {'mensaje':'error - datos invalidos'}

    return {'mensaje':'recibido'}


if __name__ == "__main__":
    app.run(debug=True)