def generate_email(event_name, start_date, end_date, venue, time, event_type, meet_link=None):
    # Constructing date range text
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
