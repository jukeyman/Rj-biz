from flask import render_template
from app import app

@app.route('/blog')
def blog1():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render_template("blog/blog1.html", **data)

@app.route('/blog2')    
def blog2():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render_template("blog/blog2.html", **data)
    
@app.route('/blog3')    
def blog3():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render_template("blog/blog3.html", **data)
    
@app.route('/blog4')    
def blog4():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render_template("blog/blog4.html", **data)
    
@app.route('/blog-details')    
def blogDetails():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'breadcrumb' : 'false'
    }
    return render_template("blog/blogDetails.html", **data)
    