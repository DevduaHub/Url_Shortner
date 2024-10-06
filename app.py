from flask import Flask, request, render_template, redirect
import string
import random

app = Flask(__name__)

# In-memory dictionary to store short URL mappings
url_dict = {}

# Function to generate random short ID
def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Route for the home page and shortening URLs
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_id = generate_id()
        url_dict[short_id] = original_url  # Store in dictionary
        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

# Redirecting short URL to the original URL
@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_dict.get(short_id)  # Retrieve from dictionary
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
