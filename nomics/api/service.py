from dateutil.parser import parse

def format_date(date_string):
    date = parse(date_string).replace(tzinfo=None).isoformat()
    date = date.split('+')[0] + 'Z'

    return date


