import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('grocery_list')

print("Welcome to your Grocery list.")


def create_new_list():
    """
    Add a worksheet for a new grocery list and name it based on user input.
    """
    new_list = input("Please enter a name for the list: ")
    SHEET.add_worksheet(title = new_list, rows="100", cols="20")

create_new_list()