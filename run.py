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
    return new_list

grocery_list = create_new_list()


def list_menu():
    """
    Provide user a menu option to add more items to the list or exit the app.
    """
    print("[1] Add+")
    print("[2] Exit")
    option = int(input("Enter option: "))
    return option


def get_list():
    """
    Get grocery items, quantity and measurement from user input and add to list.
    """
    option = list_menu()
   
    while option != 2:
        if option == 1:
            grocery_item = []
            item = input("Enter item name: ")
            grocery_item.append(item)
            quantity = int(input("Enter quantity: "))
            grocery_item.append(quantity)
            unit_of_measurement = input("Enter unit of measurement: ")
            grocery_item.append(unit_of_measurement)
            print(f"Adding {item} to list...")
            update_list = SHEET.worksheet(grocery_list)
            update_list.append_row(grocery_item)
            print(f"{item} added.\n")
        else:
            print("Invalid option.\n")
        
        option = list_menu()

    print("Your list have been updated.")

get_list()


