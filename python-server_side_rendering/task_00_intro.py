#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("The template is a string")
        return
    if not isinstance(attendees, list):
        print("Attendees are a list of dictionaries")
        return
    if not template:
        print("The Template is empty, no output file is generated")
        return
    if not attendees:
        print("The Template is empty, no output file is generated")
        return

    for x, attende in enumerate(attendees, start=1):
        content = template
        content = content.replace("{name}", attende.get("name")if attende.get("name") is not None else "N/A")
        content = content.replace("{event_title}", attende.get("event_title")if attende.get("event_title") is not None else "N/A")
        content = content.replace("{event_date}", attende.get("event_date")if attende.get("event_date") is not None else "N/A")
        content = content.replace("{event_location}", attende.get("event_location")if attende.get("event_location") is not None else "N/A")

        output_files = f"output_{x}.txt"

        if os.path.exists(output_files):
            print(f"Error: {output_files} already exists. Skipping")
            continue

        try:
            with open(output_files, 'w') as file:
                file.write(content)
            print(f"Generated {output_files}")
        except Exception as e:
            print(f"Error writing to {output_files}: {e}")
