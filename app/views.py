from app import app
from flask import render_template,send_from_directory


@app.route('/')
@app.route('/index')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')