import os

def generate_invitations(template, attendees):
    # 1. Input tipini yoxla
    if not isinstance(template, str):
        print(f"Error: Template should be a string, got {type(template)}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees should be a list of dictionaries, got {type(attendees)}")
        return

    # 2. Boş girişləri yoxla
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir iştirakçını işləmək
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        # 4. Faylı yaz
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(invitation)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
