from flask import Flask, jsonify, request
app = Flask(__name__)
# Home (/) route
@app.route('/')
def home():
    return"""
           <h1>User Portal</h1>
           <a href = "/user/Nimit" class = "btn btn-primary">Go to Nimit's User Page</a><br>
           <a href = "/age/15" class = "btn btn-primary">Go to Nimit's Age</a><br>
           <a href = "/profile/Nimit/15" class = "btn btn-primary">Go to Nimit's Profile</a><br>
           <a href = "/search?skill=python" class = "btn btn-primary">Search Nimit's Skill</a><br>
           <a href = "/api/user/Nimit" class = "btn btn-primary">Go to Nimit's Api Endpoint</a><br>
"""
# Dynamic User Page (/user/<username>)
@app.route('/user/<username>')
def user_page(username):
    return f"Welcome, {username}"

#Age Page (Type-Safe) /age/<int:age>
@app.route('/age/<int:age>')
def age_page(age):
    return f"Your age is {age}"

# Profile Page (Multiple Params) /profile/<username>/<int:age>
@app.route('/profile/<username>/<int:age>')
def profile_page(username,age):
    return f"User: {username}<br> Age: {age}"
#Search Page (GET Parameter) '/search'
@app.route('/search')
def search_page():
    skill = request.args.get('skill') #/search?skill=python
    if skill == None:
        return "No search query provided"
    return f"You searched for skill: {skill}"

# API Endpoint (JSON) Route: /api/user/<username>
@app.route('/api/user/<username>')
def api_user(username):
    return jsonify (
        {
           "username": username,
           "status": "active"
       }
    )

if __name__ == "__main__":
    app.run(port = 9899, debug = True)