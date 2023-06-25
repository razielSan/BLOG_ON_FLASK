from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def get_index_page():
    return render_template('index.html')


@app.route('/html')
def get_html_page():
    return render_template('html_page.html')


@app.route('/css')
def get_css_page():
    return render_template('css_page.html')


@app.route('/django')
def get_django_page():
    return render_template('django_page.html')


@app.route('/flask')
def get_flask_page():
    return render_template('flask_page.html')


@app.route('/js')
def get_js_page():
    return render_template('js_page.html')


@app.route('/python')
def get_python_page():
    return render_template('python_page.html')


if __name__ == '__main__':
    app.run(debug=True)
