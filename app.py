from flask import Flask, request, render_template, redirect, url_for
from mail import generate_email  # Import the generate_email function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_event_type', methods=['POST'])
def select_event_type():
    event_type = request.form['event_type']
    if event_type == 'online':
        return redirect(url_for('online_event_form'))
    else:
        return redirect(url_for('offline_event_form'))

@app.route('/online_event_form')
def online_event_form():
    return render_template('online_form.html')

@app.route('/offline_event_form')
def offline_event_form():
    return render_template('offline_form.html')

@app.route('/generate', methods=['POST'])
def generate():
    event_name = request.form['event_name']
    start_date = request.form['start_date']
    end_date = request.form.get('end_date', '')  # Use .get() to handle missing 'end_date'
    venue = request.form.get('venue', '')  # Venue might not be needed for online events
    time = request.form['time']
    event_type = request.form['event_type']
    meet_link = request.form.get('meet_link', '')  # Get the Google Meet link for online events

    email = generate_email(event_name, start_date, end_date, venue, time, event_type, meet_link)
    return email

if __name__ == '__main__':
    app.run(debug=True)
