from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'RJ Business Solutions',
        'subTitle': 'Complete Business Solutions',
    }
    return render_template("home/index.html", **data)

@app.route('/services')
def services():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Our Services',
        'subTitle': 'Complete Business Solutions',
    }
    return render_template("pages/services/service.html", **data)

@app.route('/about')
def about():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'About Us',
        'subTitle': 'About RJ Business Solutions',
    }
    return render_template("pages/about.html", **data)

@app.route('/contact')
def contact():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Contact Us',
        'subTitle': 'Get in Touch',
    }
    return render_template("pages/contact.html", **data)

@app.route('/portfolio')
def portfolio():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Our Portfolio',
        'subTitle': 'Client Success Stories',
    }
    return render_template("pages/projects/portfolio1.html", **data)

@app.route('/faq')
def faq():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'FAQs',
        'subTitle': 'Frequently Asked Questions',
    }
    return render_template("pages/faq.html", **data)

@app.route('/pricing')
def pricing():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Our Pricing',
        'subTitle': 'Service Packages',
    }
    return render_template("pages/pricing.html", **data)

@app.route('/privacy')
def privacy():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Privacy Policy',
        'subTitle': 'Privacy Policy',
    }
    return render_template("pages/utility/privacy.html", **data)

@app.route('/terms')
def terms():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Terms of Service',
        'subTitle': 'Terms of Service',
    }
    return render_template("pages/utility/terms.html", **data)

@app.route('/blog')
def blog():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Our Blog',
        'subTitle': 'Latest Updates',
    }
    return render_template("blog/blog1.html", **data)

@app.route('/error')
def error():
    data = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': '404 Error',
        'subTitle': 'Page Not Found',
        'header': 'false',
        'footer': 'false',
    }
    return render_template("pages/utility/error.html", **data)

