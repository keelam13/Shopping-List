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

def main_menu():
    """
    Provides user option to add new grocery list, view existing lists, or exit app.
    """
    print("[0] Exit")
    print("[1] Add new list")
    print("[2] View lists")
    main_option = int(input("Enter option: "))
    print()
    return main_option


def get_lists():
    """
    Get all worksheets from the spreadsheet.
    """
    sheet_num = 0
    for sheet in SHEET:
        sheet_num += 1
        print(f"[{sheet_num}]", sheet.title)


def view_lists():
    """
    Shows data from selected list.
    """
    get_lists()
    select_list = int(input("Select list: ")) - 1
    selected_list = SHEET.get_worksheet(select_list)
    view_data = selected_list.get_all_values()
    print()
    print(view_data)


def list_menu():
    """
    Provide user a menu option to add more items to the list or exit the app.
    """
    print("[1] Add+")
    print("[2] Exit")
    list_option = int(input("Enter option: "))
    print()
    return list_option


def create_new_list():
    """
    Add a worksheet for a new grocery list and name it based on user input.
    Add headings to the worksheet.
    """
    new_list = input("Please enter a name for the list: ")
    new_worksheet = SHEET.add_worksheet(title = new_list, rows="100", cols="20")
    heading = ["Items", "Quantity", "Measurement"]
    new_worksheet.append_row(heading)
    return new_list


def get_list(grocery_list):
    """
    Get grocery items, quantity and measurement from user input and add to list.
    Function will loop while user chooses to add more items otherwise exit the loop.
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

    print("Your list have been updated.\n")



def delete_list():
    """
    Select and delete existing list
    """
    
def main():
    """
    Run all program functions.
    """
    option = main_menu()
    while option != 0:
        if option == 1:
            grocery_list = create_new_list()
            get_list(grocery_list)
        elif option == 2:
           view_lists()
        else:
            print("Invalid option\n")
        
        option = main_menu()

    print("Until next time, good bye!" )


print("Welcome to your Grocery list.\n")

main()

