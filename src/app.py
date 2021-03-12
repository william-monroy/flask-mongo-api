from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://admin:NnolascO123@cluster0.3i7nq.mongodb.net/Pruebas?retryWrites=true&w=majority'

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