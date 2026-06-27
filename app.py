from flask import Flask, render_template, send_from_directory
from flask_talisman import Talisman
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

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
        '\'self\'',
        '\'unsafe-inline\''
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

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml', mimetype='application/xml')

if __name__ == '__main__':
    app.run()
