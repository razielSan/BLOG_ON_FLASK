from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/html')
def html_page():
    return render_template('html_page.html')


@app.route('/django')
def djano_page():
    return render_template('django_page.html')


@app.route('/css')
def css_page():
    return render_template('css_page.html')


@app.route('/python')
def python_page():
    return render_template('python_page.html')


@app.route('/js')
def js_page():
    return render_template('js_page.html')


@app.route('/flask')
def flask_page():
    return render_template('flask_page.html')


if __name__ == '__main__':
    app.run(debug=True)
