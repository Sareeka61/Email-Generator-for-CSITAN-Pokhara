from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Display the form

@app.route('/generate', methods=['POST'])
def generate_email():
    recipient_type = request.form.get('recipient_type')  # Get the selected recipient type from the form

    # Process form data and generate email content based on recipient type
    if recipient_type == 'participants':
        email_content = generate_participant_email(request.form)
    elif recipient_type == 'mentors':
        email_content = generate_mentor_email(request.form)
    elif recipient_type == 'volunteers':
        email_content = generate_volunteer_email(request.form)
    else:
        email_content = "Invalid recipient type"

    return render_template('generated_email.html', email_content=email_content)

def generate_participant_email(form_data):
    event_name = form_data['event_name']
    start_date = form_data['start_date']
    end_date = form_data.get('end_date')
    venue = form_data['venue'] if form_data['event_type'] == 'offline' else ''
    time = form_data['time']
    event_type = form_data['event_type']
    meet_link = form_data.get('meet_link')

    if end_date:
        date_range = f"{start_date} to {end_date}"
    else:
        date_range = start_date

    # Constructing venue and meet link text based on event type
    if event_type == "offline":
        venue_text = f" at {venue}"
        meet_link_text = ""
    else:
        venue_text = ""
        meet_link_text = f"Google Meet Link: {meet_link}\n"

    # Constructing the email template
    email_template = f"""
    CSIT ASSOCIATION OF NEPAL - POKHARA

    Dear participants,

    We hope this mail finds you well! We would like to invite you to a "{event_name}" happening on {date_range}{venue_text}. Thank you for your enthusiasm. We hope for your active participation in this workshop with insightful queries. Please be on time and find the event details below.

    Event Details:-

    Venue: {venue}
    Date: {date_range}
    Time: {time}
    {meet_link_text}

    We hope you have a great time learning! Your assistance will be highly appreciated.

    Feel free to contact us in case of any queries.

    Best regards,
    President
    CSITAN Pokhara
    """

    return email_template

def generate_volunteer_email(form_data):
    event_name = form_data['event_name']
    start_date = form_data['start_date']
    end_date = form_data.get('end_date')
    venue = form_data['venue'] if form_data['event_type'] == 'offline' else ''
    time = form_data['time']
    event_type = form_data['event_type']
    meet_link = form_data.get('meet_link')

    if end_date:
        date_range = f"{start_date} to {end_date}"
    else:
        date_range = start_date

    # Constructing venue and meet link text based on event type
    if event_type == "offline":
        venue_text = f" at {venue}"
        meet_link_text = ""
    else:
        venue_text = ""
        meet_link_text = f"Google Meet Link: {meet_link}\n"
    # Constructing the email template for volunteers
    email_template = f"""
    CSIT ASSOCIATION OF NEPAL - POKHARA

    Dear sir/ma'am,

    We are glad to inform you that you are selected as a volunteer for the "{event_name}" organized by CSIT Association of Nepal- Pokhara happening on {date_range} at {venue}. Thank you for your enthusiasm and willingness to support the community. We hope for your active participation in this workshop.

    Event details:

    Venue: {venue}
    Date: {date_range}
    Time: {time}
    {meet_link_text}

    Your assistance will be highly appreciated. Please be on time. Thank you!

    Feel free to contact us in case of any queries.

    Best regards,
    President
    CSITAN Pokhara
    """

    return email_template


def generate_mentor_email(form_data):
    event_name = form_data['event_name']
    start_date = form_data['start_date']
    end_date = form_data.get('end_date')
    venue = form_data['venue'] if form_data['event_type'] == 'offline' else ''
    time = form_data['time']
    event_type = form_data['event_type']
    meet_link = form_data.get('meet_link')

    if end_date:
        date_range = f"{start_date} to {end_date}"
    else:
        date_range = start_date

    # Constructing venue and meet link text based on event type
    if event_type == "offline":
        venue_text = f" at {venue}"
        meet_link_text = ""
    else:
        venue_text = ""
        meet_link_text = f"Google Meet Link: {meet_link}\n"

    # Constructing the email template for mentors
    email_template = f"""
    CSIT ASSOCIATION OF NEPAL - POKHARA

    Respected sir/ma'am,

    Hope this mail finds you in sound health and happiness! We are glad to share that the "{event_name}" by CSIT Association of Nepal- Pokhara happening on
 {date_range} at {venue}. We hereby cordially invite you to the workshop as our valuable mentor and would like to request your confirmation for the valuable presence in the event. Thank you for your enthusiasm and willingness to support the community.

    Event details:

    Venue: {venue}
    Date: {date_range}
    Time: {time}
    {meet_link_text}

    We will be honored by your presence and look forward to seeing you in the program. Your assistance will be highly appreciated. Please be on time. Thank you!

    Feel free to contact us in case of any queries.

    Best regards,
    President
    CSITAN Pokhara
    """

    return email_template


if __name__ == '__main__':
    app.run(debug=True)
