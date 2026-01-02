from flask import Flask, render_template
app = Flask(__name__)
# Home
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/user/<username>')
def user_page(username):
    return render_template('user.html', name = username)
@app.route('/profile/<username>/<int:age>')
def profile_page(username, age):
    return render_template('profile.html', name = username, age = age)
@app.route('/status/<username>/<int:status>')
def status_page(username, status):
    if status == 1:
        is_active = True
    else:
        is_active = False
    return render_template('status.html', user = username, status = status, active = is_active)
@app.route('/skills')
def skill_page():
    skill = ['Python', 'Flask', 'Jinja2', 'APIs', 'HTML', 'CSS']
    return render_template(
        'skills.html',
        skill = skill
    )
if __name__ == "__main__":
    app.run(port = 9899, debug = True)