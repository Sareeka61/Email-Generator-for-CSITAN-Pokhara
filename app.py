from flask import Flask, request, render_template
from mail import generate_email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    event_name = request.form['event_name']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    venue = request.form['venue']
    time = request.form['time']

    email = generate_email(event_name, start_date, end_date, venue, time)
    return email

if __name__ == '__main__':
    app.run(debug=True)
