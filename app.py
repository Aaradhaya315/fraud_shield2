from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Configure the session
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('signup.html', error="Username already exists")
        users[username] = {'password': password, 'history': []}
        session['user'] = username
        return redirect(url_for('detector'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['user'] = username
            return redirect(url_for('detector'))
        return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/detector', methods=['GET', 'POST'])
def detector():
    if 'user' not in session:
        return redirect(url_for('login'))

    result = ''
    if request.method == 'POST':
        user_input = request.form['input'].lower()
        is_fraud = check_fraud(user_input)
        result = 'Potentially Unsafe' if is_fraud else 'Safe'
        
        # Save the search result to user's search history
        users[session['user']]['history'].append({'input': user_input, 'result': result})

    return render_template('index.html', result=result, history=users[session['user']]['history'])

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('profile.html', username=session['user'])

def check_fraud(user_input):
    fraud_keywords = [
        'fraud', 'scam', 'phishing', 'malware', 'unsafe', 
        'won', 'lottery', 'inheritance', 'prize', 'claim', 
        'offer', 'free', 'click', 'login', 'password', 
        'account', 'urgent'
    ]
    for keyword in fraud_keywords:
        if keyword in user_input:
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/login', methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Provided username:", username)  # Debug statement
        print("Provided password:", password)  # Debug statement
        if username in users:
            print("Stored password:", users[username]['password'])  # Debug statement
            if users[username]['password'] == password:
                session['user'] = username
                return redirect(url_for('detector'))
        return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

