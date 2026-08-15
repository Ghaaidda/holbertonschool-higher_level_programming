import os

def generate_invitations(template, attendees):
    """
    Generates invitations from a predefined template.
    """
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Error: Invalid input types.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for ind, attendee in enumerate(attendees, start=1):
        try:
            name = attendee.get('name', 'N/A')
            event_title = attendee.get('event_title', 'N/A')
            event_location = attendee.get('event_location', 'N/A')
            event_date = attendee.get('event_date', 'N/A')

            invitation = template.replace("{name}", name)
            invitation = invitation.replace("{event_title}", event_title)
            invitation = invitation.replace("{event_location}", event_location)
            invitation = invitation.replace("{event_date}", event_date)

            if not os.path.exists(f"output_{ind}.txt"):
                with open(f"output_{ind}.txt", "x") as f:
                    f.write(invitation)

        except KeyError as e:
            print(f"Missing field {e} for attendee, skipping.")

