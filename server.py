from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
# Route for page navigation.
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csv_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(csv_file, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email, subject, message])

# Route to handle the POST/GET events.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'
