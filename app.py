from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\''
    ],
    'style-src': [
        '\'self\'',
        'fonts.googleapis.com',
        'cdnjs.cloudflare.com',
        '\'unsafe-inline\''
    ],
    'font-src': [
        '\'self\'',
        'fonts.gstatic.com',
        'cdnjs.cloudflare.com'
    ],
    'script-src': [
        '\'self\''
    ],
    'img-src': [
        '\'self\'',
        'data:'
    ]
}

Talisman(app, force_https=False, content_security_policy=csp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
