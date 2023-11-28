import requests
import csv
import json
import sys
import re


def get_prerequisites(crn):
    lookup_url = 'https://classes.oregonstate.edu/api/?page=fose&route=details'
    lookup_payload = {'key': f'crn:{crn}'}

    encoded_payload = json.dumps(lookup_payload)

    response = requests.post(lookup_url, data=encoded_payload)

    if response.status_code == 200:
        try:
            course_data = response.json()

            registration_restrictions = course_data.get('registration_restrictions', {})
            registration_restrictions = re.sub(r'<[^>]*>', '', registration_restrictions)

            return registration_restrictions
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
    else:
        print(f"Error: Failed to fetch course data for CRN {crn}")


if len(sys.argv) != 2:
    print("Usage: python micro.py <CRN>")
    sys.exit(1)

# Extract CRN with command-line
crn_to_lookup = sys.argv[1]

registration_restrictions = get_prerequisites(crn_to_lookup)

if registration_restrictions:
    output_filename = f"registration_restrictions_{crn_to_lookup}.csv"
    with open(output_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['CRN', 'Registration Restrictions'])

        csv_writer.writerow([crn_to_lookup, json.dumps(registration_restrictions)])

    print(f"Registration restrictions for CRN {crn_to_lookup} written to {output_filename}")
else:
    print(f"Failed to retrieve registration restrictions for CRN {crn_to_lookup}")