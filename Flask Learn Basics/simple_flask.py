from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Home page</h1><a href = '/name'>Name</a> <a href = '/info'>Info</a>"
@app.route("/name")
def name():
    return "<h1>My name is <strong>Nimit Biswas</strong></h1><a href = '/'>Home</a> <a href = '/info'>Info</a>"
@app.route("/info")
def info():
    return jsonify({
        "name":"Nimit Biswas",
        "age": 15
        })
@app.route("/name/<username>")
def username(username):
    return f"<h2>Hi <h1><strong>{username}</strong></h1></h2>"
@app.route("/age/<int:user_age>")
def age(user_age):
    return f"<h1> User Age = {user_age} </h1>"
@app.route("/profile/<username>/<int:age>")
def profile(username,age):
    return f"""<marquee><h1> Welcome to Profile Page</h1><br></marquee>
            <h2>Profile Details</h2>
            <p>Username: {username}</p><br>
            <p>Age: {age}</p>
"""
@app.route("/search")
def search():
    item = request.args.get("item")
    return f"You have searched for {item}" #/search?item=value
@app.route("/filter")
def filter():
    item = request.args.get("item")
    price = request.args.get("price")
    return f"Item: {item} Price: {price}" #/filter?item=value&price=value
if __name__ == "__main__":
    app.run(port = 9899, debug = True)
