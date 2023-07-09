from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
def get_index_page():
    return render_template('index.html')


@main.route('/blog')
def get_blog():
    return render_template('index.html')


@main.route('/html')
def get_html_page():
    return render_template('html_page.html')


@main.route('/css')
def get_css_page():
    return render_template('css_page.html')


@main.route('/django')
def get_django_page():
    return render_template('django_page.html')


@main.route('/flask')
def get_flask_page():
    return render_template('flask_page.html')


@main.route('/js')
def get_js_page():
    return render_template('js_page.html')


@main.route('/python')
def get_python_page():
    return render_template('python_page.html')
