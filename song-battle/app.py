from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['DEBUG'] = True  # Set to False in production

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/api/health')
def health():
    """checkpoint"""
    return jsonify({'status': 'healthy', 'message': 'Flask app is running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

