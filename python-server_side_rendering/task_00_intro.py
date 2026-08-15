import os

def generate_invitations(template, attendees):
    """
    Generates invitations from a predefined template.
    """
    if not isinstance(template, str) or not isinstance(attendees, list):
        raise TypeError("Error: Invalid input types.")

    if not template or not attendees:
        raise ValueError("Error: Template and attendees list cannot be empty.")


    for ind, attendee in enumerate(attendees):
        try:
            invitation = template.replace("{name}", attendee['name'])
            invitation = invitation.replace("{event_title}", attendee['event_title'])
            invitation = invitation.replace("{event_location}", attendee['event_location'])

            if not os.path.exists(f"output_{ind}.txt"):
                with open(f"output_{ind}.txt", "x") as f:
                    f.write(invitation)

        except KeyError as e:
            print(f"Missing field {e} for attendee, skipping.")

