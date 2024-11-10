import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('grocery_list')

def menu(message, *arg):
    """
    Provides user a menu option for navigation.
    """
    option_num = -1
    for i in arg:
        option_num += 1
        print(f"[{option_num}] {i}")
    num_of_options = len(arg)
    list_option = validate_data_input(menu, message, num_of_options)
    print()
    return list_option


def get_lists():
    """
    Gets all worksheets from the spreadsheet.
    """
    sheet_num = 0
    for sheet in SHEET:
        sheet_num += 1
        print(f"[{sheet_num}]", sheet.title)
    num_of_options = len(SHEET.worksheets())
    select_list = validate_data_input(menu,  "Please enter a list number: ", num_of_options) - 1
    get_list = SHEET.get_worksheet(select_list)
    return get_list


def get_list_item(grocery_list):
    """
    Locates the item enetered by user from the list.
    """
    entered = validate_data_input("item", "Enter item name: ")
    item = grocery_list.find(entered)
    return item


def get_item_input(grocery_list):
    """
    Gets grocery items, quantity and measurement from user input and add to list.
    Function will loop while user chooses to add more items otherwise exit the loop.
    """
    grocery_item = []
    item = validate_data_input("item", "Enter item name: ")
    grocery_item.append(item)
    quantity = validate_data_input("qty", "Enter quantity: ")
    grocery_item.append(quantity)
    unit_of_measurement = validate_data_input("unit", "Enter unit of measurement: ")
    grocery_item.append(unit_of_measurement)
    print(f"Adding {item} to list...")
    update_list = SHEET.worksheet(grocery_list)
    update_list.append_row(grocery_item)
    print(f"{item} added.\n")
    

def view_lists():
    """
    Shows data of selected list in a table.
    """
    selected_list = get_lists()
    view_data = selected_list.get_all_values()
    print()
    print(f"Viewing {selected_list.title} list")
    print(tabulate(view_data),"\n")
    return selected_list


def delete_data(data, grocery_list):
    """
    Deletes a selected data and asks user to confirmdeletion.
    """
    if data == "list":
        print(f"Are you sure you want to delete {grocery_list.title}?")
        confirm = menu("Please enter option number: ", "No", "Yes")
        while confirm != 0:
            if confirm == 1:
                print(f"Deleting {data}...\n")
                SHEET.del_worksheet(grocery_list)
                print(f"{data.capitalize()} successfully deleted.\n")
            else:
                print("Invalid option")
            break
    elif data == "item":
        cell = get_list_item(grocery_list)
        print(f"Are you sure you want to delete {cell.value}?")
        confirm = menu("Please enter option number: ", "No", "Yes")
        while confirm != 0:
            if confirm == 1:
                print(f"Deleting {data}...\n")
                grocery_list.delete_rows(cell.row)
                print(f"{data.capitalize()} successfully deleted.\n")
            else:
                print("Invalid option")
            break
    else:
        print("Invalid option")


def create_new_list():
    """
    Adds a worksheet for a new grocery list and name it based on user input.
    Adds headings to the worksheet.
    """
    new_list = validate_data_input("list", "Please enter a name for the list: ")
    new_worksheet = SHEET.add_worksheet(title = new_list, rows="100", cols="20")
    heading = ["Items", "Quantity", "Measurement"]
    new_worksheet.append_row(heading)
    return new_list


def validate_data_input(*args):

    while True:
        if len(args) == 2:
            if args[0] == "qty":
                try:
                    data_input = float(input(args[1]))
                    return data_input
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            else:
                try:
                    item_input = input(args[1]).strip()
                    if len(item_input) >= 3:
                        return item_input
                    else:
                        print("Invalid input.")
                        print("Please enter atleast 3 characters.")
                except:
                    print("Invalid input.")
                    print("Please enter atleast 3 characters.")
        else:    
            try:
                select_num = int(input(args[1]))
                if select_num <= args[2] and select_num >= 0:
                    return select_num
                else:
                    print("Invalid input. Please enter a number from the options.")
            except ValueError:
                print("Invalid input. Please enter a number from options.")


def main():
    """
    Run all program functions.
    """
    option = menu("Please enter option number: ", "Exit", "Add new list", "View lists", "Delete list")
    while option != 0:
        if option == 1:
            new_grocery_list = create_new_list()
            ticked = menu("Please enter option number: ", "Exit", "Add items")
            while ticked != 0:
                get_item_input(new_grocery_list)
                ticked = menu("Please enter option number: ", "Exit", "Add+")
            print("Your list have been updated.\n")
        elif option == 2:
            selected_list = view_lists()
            to_do = menu("Please enter option number: ", "Exit", "Add new item", "Edit an item", "Delete an item")
            while to_do != 0:
                if to_do == 1:
                    get_item_input(selected_list.title)  
                elif to_do == 2:
                    print("Option 2 has been called")
                elif to_do == 3:
                    delete_data("item", selected_list)
                else:
                    print("Invalid input. Please enter a number from options.")
                to_do = menu("Please enter option number: ", "Exit", "Add+", "Edit an item", "Delete an item")
            print("Your list have been updated.\n") 
        elif option == 3:
            selected_list = view_lists()
            delete_data("list", selected_list)
        else:
            print("Invalid input. Please enter a number from options.")
        
        option = menu("Please enter option number: ", "Exit", "Add new list", "View lists", "Delete list")

    print("Until next time, good bye!")


print("Welcome to your Grocery list.\n")

main()