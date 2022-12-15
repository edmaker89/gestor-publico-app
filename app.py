from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required



app = Flask(__name__)

#Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'edmaker-secret-key'
jwt = JWTManager(app)

# Our protected route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username != 'edmaker' or password != 'edmaker':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    print(access_token)
    return redirect('/protected')
    #return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acessos')
def acessos():
    return render_template('acessos.html')

@app.route('/gsp/home')
def gsp_home():
    return render_template('/gsp/index.html')

@app.route('/gsp/pessoas')
def gsp_pessoas():
    return render_template('/gsp/pessoas.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)