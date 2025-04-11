import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# If modifying this file, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # Use read-write scope if needed

def authenticate():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is created automatically
    # when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use the environment variable to dynamically get the Codespace name
            codespace_url = os.getenv("CODESPACE_NAME", "localhost")
            redirect_uri = f"https://{codespace_url}.github.dev/oauth2/callback"
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_client_secret.json', SCOPES, redirect_uri=redirect_uri)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def read_google_sheet(spreadsheet_id, range_name):
    creds = authenticate()
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    return values

if __name__ == '__main__':
    # Replace with your actual spreadsheet ID and range
    spreadsheet_id = 'your-spreadsheet-id'
    range_name = 'Sheet1!A1:D10'  # Adjust the range according to your sheet
    values = read_google_sheet(spreadsheet_id, range_name)
    if not values:
        print('No data found.')
    else:
        for row in values:
            print(row)