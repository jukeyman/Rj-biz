from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    data={
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>'
    }
    return render_template("home/index.html", **data)

@app.route('/index2')
def index2():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/clash-grotesk/style.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass': 'bg-[#F6F5EF]',
        'header': 'false',
        'footer': 'false'
    }
    return render_template("home/index2.html", **data)

@app.route('/index3')
def index3():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/familjen-grotesk/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass': 'bg-[#FEFCFB]',
        'header': '',
        'footer': 'false'
    }
    return render_template("home/index3.html", **data)

@app.route('/index4')
def index4():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/arimo/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/offcanvas-menu.js"></script>',
        'bodyClass':'bg-[#FFF7EA]',
        'header':'false',
        'footer':'false'
    }
    return render_template("home/index4.html", **data)


@app.route('/index5')
def index5():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/libre-baskerville/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#FFFCF2]',
        'header':'false',
        'footer':'false'
    }
    return render_template("home/index5.html", **data)


@app.route('/index6')
def index6():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/playfair-display/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-white',
        'header':'false',
        'footer':'false'
    }
    return render_template("home/index6.html", **data)


@app.route('/index7')
def index7():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/bricolage-grotesque/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#F8FCDD]',
        'header':'false',
        'footer':'false'
    }
    return render_template("home/index7.html", **data)


@app.route('/index8')
def index8():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/outfit/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#FCF9F0]',
        'header':'false',
        'footer':'false'
    }
    return render_template("home/index8.html", **data)


@app.route('/index9')
def index9():
    data = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/epilogue/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#FEF6E0]',
        'header':'false',
        'footer':'false'
    }
    return render_template("home/index9.html", **data)
