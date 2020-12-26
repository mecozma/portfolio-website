import os
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'The form has been submitted.'
