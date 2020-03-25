from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1OVf8YkHpIwIZaYzJB-uwU7HXjs0GbSZYQyN9UEwQZ2U'
SAMPLE_RANGE_NAME = 'Active!A4:V'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Paygrade,FirstName,LastName,AOR,Status,SpecialStatus,BootGrad,PFCPromo,SPCPromo,CPLPromo,GC1,'
              'Bronze1,Bronze2,Bronze3,Silver1,Silver2,Silver3,Gold1,Gold2,Gold3')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(row[0], row[2], row[3], row[4], row[5], row[8], row[9], row[10], row[11], row[12], row[13],
                  row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21])


if __name__ == '__main__':
    main()
