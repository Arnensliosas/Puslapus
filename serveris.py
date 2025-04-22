from flask import Flask, render_template, request, flash, redirect, url_for
import csv

app = Flask(__name__)
app.secret_key = 'very nesecret key' # didelis bbz kam sitas cia chat gpt cookino reikes issiaiskinti

def hashinimas(passwordas):
    zodis = "12a321185654ambatakumas45atvaziuoja3jistuoj843atvaziuos9f4h456dfh89g"
    listas = []
    vidur = len(passwordas) // 2 + 1
    passw = passwordas[:vidur] + zodis + passwordas[vidur:]
    for i in passw:
        ans = ord(i) // 2 + 7
        ans = ans % 126 + 29
        listas.append(ans)
    sudas = "".join(map(chr, listas))
    return sudas

@app.route('/')
def login():
    return render_template('index.html')  

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/namuDarbai')
def game():
    return render_template('namuDarbai.html')


# Handle login POST
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    passwordas_loginui = hashinimas(password)

    with open('puslapus/users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [username, passwordas_loginui]:
                return redirect(url_for('game'))
    
    flash("❌ ot ir neteisingai ivedei kazka")
    return redirect(url_for('login'))


# Handle register POST
@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form.get('reg-username')
    password = request.form.get('reg-password')
    passwordas = hashinimas(password)

    with open('puslapus/users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, passwordas])

    print(f"Registeration info: {username}, {password}")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

