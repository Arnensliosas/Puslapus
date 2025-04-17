from flask import Flask, render_template, request

app = Flask(__name__)

# Show login form
@app.route('/')
def login():
    return render_template('index.html')  # This is your login page

# Show registration form
@app.route('/register')
def register():
    return render_template('register.html')

# Handle login POST
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Login: {username}, {password}")
    return "Login info received"

# Handle register POST
@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form.get('reg-username')
    password = request.form.get('reg-password')
    print(f"Register: {username}, {password}")
    return "Registration info received"


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)