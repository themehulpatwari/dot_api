import requests
from icalendar import Calendar

def get_ics_events(ics_url: str) -> list[dict]:
    
    """
    Fetches and parses events from an ICS (iCalendar) file located at the given URL.
    Args:
        ics_url (str): The URL of the ICS file to fetch.
    Returns:
        dict: A dictionary containing the parsed events. Each event is represented as a dictionary with the following keys:
            - summary (str or None): The summary or title of the event.
            - start (datetime or None): The start date and time of the event.
            - end (datetime or None): The end date and time of the event.
            - location (str or None): The location of the event.
            - description (str or None): A description of the event.
    Raises:
        Exception: If the ICS file cannot be fetched or if the response status code is not 200.
    """

    # Fetch the .ics file from the given URL
    response = requests.get(ics_url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the ics file. Status code: {response.status_code}")
    
    # Parse the ICS content
    cal = Calendar.from_ical(response.content)
    
    events = []
    
    for component in cal.walk():
        if component.name == "VEVENT":
            event = {
                "summary": str(component.get('summary')) if component.get('summary') else None,
                "start": component.get('dtstart').dt if component.get('dtstart') else None,
                "end": component.get('dtend').dt if component.get('dtend') else None,
                "location": str(component.get('location')) if component.get('location') else None,
                "description": str(component.get('description')) if component.get('description') else None
            }
                
            events.append(event)
    
    return events