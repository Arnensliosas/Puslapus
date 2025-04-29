from flask import Flask, render_template, request, abort, redirect, url_for, session, jsonify
import bcrypt
import csv

app = Flask(__name__)
app.secret_key = 'ur either perfect or ur not me' # didelis bbz kam sitas cia chat gpt cookino reikes issiaiskinti

@app.route('/')
def login():
    return render_template('index.html')  

@app.route('/register')
def register():
    print(session)
    return render_template('register.html')

@app.route('/namuDarbai')
def game():
    print(session)
    if 'username' not in session:
        abort(401)
    return render_template('namuDarbai.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# Handle login POST
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_username = row[0]
            stored_hash = row[1]
            if username == stored_username:
                if bcrypt.checkpw(password.encode(), stored_hash.encode()): 
                    session['username'] = username
                    return jsonify({"success": True})

    return jsonify({"success": False, "message": "❌ ot ir neteisingai ivedei kazka"})


# Handle register POST
@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form.get('reg-username')
    password = request.form.get('reg-password')

    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if username == row[0]:
                return jsonify({"success": False, "message": "toks vardas jau egzistuoja"})
            
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password.decode('utf-8')])

    return jsonify({"success": True, "message": "mldc prisiregistravai"})


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

