#!/usr/bin/python3

def generate_invitations(template, attendees):
    # Check if the template is a string; if not, print an error and exit.
    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return

    # Check if attendees is a list; if not, print an error and exit.
    if not isinstance(attendees, list):
        print("Error: Attendees must be provided as a list.")
        return

    # Check if the template is empty; if so, print an error and exit.
    if not template:
        print("Error: Template is empty; no output files created.")
        return

    # Check if the attendees list is empty; if so, print an error and exit.
    if not attendees:
        print("Error: No attendee data provided; no output files created.")
        return

    # Iterate over each attendee, starting the index at 1.
    for idx, attendee in enumerate(attendees, start=1):
        content = template  # Copy the template content for modification.

        # Replace placeholders in the template with values from the attendee.
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            # Get the value from the attendee dictionary; use "N/A" if missing.
            value = attendee.get(placeholder, "N/A")
            # Replace the placeholder in the content
            # with the actual value or "N/A".
            content = content.replace(
                f"{{{placeholder}}}", value if value else "N/A"
            )

        # Create an output filename based on the current index.
        output_filename = f"output_{idx}.txt"

        # Write the modified content to the output file.
        with open(output_filename, "w") as output_file:
            output_file.write(content)

        # Print a message indicating the file has been created.
        print(f"File created: {output_filename}")
