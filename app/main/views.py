from flask import render_template, url_for, redirect


def index_page():
    return render_template('index.html')


def redirect_page():
    return redirect(url_for('main.index_page'))
