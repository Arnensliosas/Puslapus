from flask import Flask, render_template, request, flash
import csv

app = Flask(__name__)
app.secret_key = 'very nesecret key' # didelis bbz kam sitas cia chat gpt cookino reikes issiaiskinti


@app.route('/')
def login():
    return render_template('index.html')  

@app.route('/register')
def register():
    return render_template('register.html')

# Handle login POST
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [username, password]:
                return render_template('/namuDarbai.html')
    
    flash("❌ ot ir neteisingai ivedei kazka")
    return render_template('index.html')


# Handle register POST
@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form.get('reg-username')
    password = request.form.get('reg-password')

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print(f"Registeration info: {username}, {password}")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)