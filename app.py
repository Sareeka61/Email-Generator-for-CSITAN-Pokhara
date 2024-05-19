from flask import Flask, request, render_template, redirect, url_for
from mail import generate_participant_email, generate_mentor_email, generate_volunteer_email

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
    recipient_type = request.form['recipient_type']  # Get the selected recipient type
    if recipient_type == 'participants':
        email_content = generate_participant_email(request.form)
    elif recipient_type == 'mentors':
        email_content = generate_mentor_email(request.form)
    elif recipient_type == 'volunteers':
        email_content = generate_volunteer_email(request.form)
    else:
        email_content = "Invalid recipient type"

    return email_content

if __name__ == '__main__':
    app.run(debug=True)
