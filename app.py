from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from sitemap_generator import generate_sitemap
import os

app = Flask(__name__)
Bootstrap(app)

# Configure static files
app.static_folder = 'static'
app.static_url_path = '/static'

# Generate sitemap on startup
generate_sitemap()

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/service')
def service():
    return render_template('pages/services/service.html')

@app.route('/portfolio')
def portfolio():
    return render_template('pages/projects/portfolio1.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/privacy')
def privacy():
    return render_template('pages/utility/privacy.html')

@app.route('/terms')
def terms():
    return render_template('pages/utility/terms.html')

# SEO Routes
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/utility/error.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('pages/utility/error.html'), 500

if __name__ == '__main__':
    # Ensure static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(host='0.0.0.0', port=4000, debug=True)
