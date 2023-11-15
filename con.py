import requests
import base64
from datetime import datetime, timedelta

# Basic Authentication - Replace with your actual username and password
username = 'narvik.aghamalian@paysera.net'
password = '5n5R4qPHbiA%%PUcUe8d'

auth = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')

# CQL Query - Adjust as needed
cql = "type=page AND label=gpt"

# API Endpoint
url = f'https://intranet.paysera.net/rest/api/content/search?cql={cql}'

# Headers for the GET request
headers = {'Authorization': f'Basic {auth}'}

# Function to send GET request
def get_pages():
    try:
        response = requests.get(url, headers=headers)

        # Check if connected successfully
        if response.status_code == 200:
            print("Successfully connected to the server.")

            # Parsing response
            pages_data = response.json()
            results = pages_data.get('results', [])

            # Check if pages found
            if results:
                for page in results:
                    page_title = page.get('title', 'No Title')
                    page_id = page.get('id', 'No ID')
                    page_url = f'https://intranet.paysera.net/pages/viewpage.action?pageId={page_id}'
                    print(f"Found page: {page_title}, URL: {page_url}")
            else:
                print("No pages found matching the criteria.")
        else:
            print(f"Failed to connect to the server. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function
get_pages()
