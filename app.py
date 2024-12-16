import os
from flask import Flask, jsonify, render_template
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Récupération des variables d'environnement
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PAGE_ID = os.getenv('PAGE_ID')

@app.route('/')
def home():
    """Page principale."""
    return render_template('index.html')

@app.route('/get_posts', methods=['GET'])
def get_posts():
    """Récupère les publications de la page Facebook."""
    url = f"https://graph.facebook.com/v17.0/{PAGE_ID}/feed?fields=message,created_time,from&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    posts = [{'time': post.get('created_time'), 'message': post.get('message')} for post in data['data'] if 'message' in post]
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
