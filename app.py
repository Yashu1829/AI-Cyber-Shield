from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import google.generativeai as genai
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=30)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('landing'))
        return f(*args, **kwargs)
    return decorated_function

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

# Sample data
SAMPLE_PHISHING_EMAILS = [
    "URGENT: Your account has been compromised! Click here to secure: http://secure-login-now.xyz",
    "Congratulations! You've won a $1000 Amazon gift card. Claim now: http://amazon-gift.redeem-now.com",
    "Bank of America Alert: Suspicious login detected. Verify your account: http://bofa-verify-account.com"
]

SAMPLE_PASSWORDS = [
    "password123",
    "Admin@123",
    "P@ssw0rd!2023"
]

SAMPLE_URLS = [
    "http://paypal-login-secure.com/verify",
    "https://www.linkedin.com/security-update-2023",
    "http://appleid.apple.verify-account.org"
]

SAMPLE_QUESTIONS = [
    "How do I create a strong password?",
    "What is two-factor authentication?",
    "How can I detect a phishing email?"
]

# Helper functions
def analyze_phishing_email(email):
    prompt = f"Is this email likely a phishing attempt? (Yes/No/Maybe) Email: {email}"
    try:
        response = model.generate_content(prompt)
        return f"Phishing analysis: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}. Please try a shorter email or different content."

def check_password_strength(password):
    prompt = f"Rate this password strength (1-10): {password}"
    try:
        response = model.generate_content(prompt)
        return f"Password strength: {response.text}/10"
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_url(url):
    prompt = f"Is this URL potentially malicious? If this is from a real company flag it Genuine and if the url is form a unrecognised company mark it as Farud (Fraud/genuine/Maybe): {url}"
    try:
        response = model.generate_content(prompt)
        return f"URL safety check: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_response(question):
    prompt = f"Answer briefly (2-3 sentences max): {question}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}. Please try a shorter question."

# Routes
@app.route('/')
def landing():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('landing.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    return render_template('index.html',
                         username=user.username,
                         sample_emails=SAMPLE_PHISHING_EMAILS,
                         sample_passwords=SAMPLE_PASSWORDS,
                         sample_urls=SAMPLE_URLS,
                         sample_questions=SAMPLE_QUESTIONS)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists', 'error')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session.permanent = True
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('landing'))

@app.route('/analyze/email', methods=['POST'])
def analyze_email():
    email = request.json.get('email', '')
    result = analyze_phishing_email(email)
    return jsonify({'result': result})

@app.route('/analyze/password', methods=['POST'])
def analyze_password():
    password = request.json.get('password', '')
    result = check_password_strength(password)
    return jsonify({'result': result})

@app.route('/analyze/url', methods=['POST'])
def analyze_url_route():
    url = request.json.get('url', '')
    result = analyze_url(url)
    return jsonify({'result': result})

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question', '')
    result = get_ai_response(question)
    return jsonify({'result': result})

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
