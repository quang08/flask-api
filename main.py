from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>") #default is GET
def getUser(user_id):
    userData = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "johndoe@email.com"
    }
    #get query parameter /get-user/2123?extra="hello"
    extra = request.args.get("extra")
    if extra:
        userData['extra'] = extra
    return jsonify(userData), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json() #get json payload from client
    #database manipulation
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)