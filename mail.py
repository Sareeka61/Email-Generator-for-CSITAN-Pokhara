def generate_email(event_name, start_date, end_date, venue, time):
    if end_date:
        date_range = f"{start_date} to {end_date}"
    else:
        date_range = start_date

    email_template = f"""
    CSIT ASSOCIATION OF NEPAL - POKHARA

    Dear participants,

    We hope this mail finds you well! We would like to invite you to a "{event_name}" happening on {date_range} at {venue}. Thank you for your enthusiasm. We hope for your active participation in this workshop with insightful queries. Please be on time and find the event details below.

    Event Details:-

    Venue: {venue}
    Date: {date_range}
    Time: {time}

    We hope you have a great time learning! Your assistance will be highly appreciated.

    Feel free to contact us in case of any queries.

    Best regards,
    President
    CSITAN Pokhara
    """
    return email_template
